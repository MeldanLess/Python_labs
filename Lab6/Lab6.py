import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import xml.etree.ElementTree as ET
import json

def get_db_conn():
    return psycopg2.connect(
        dbname='PMC_Oreshnik_ForPython',
        user='admin',
        password='postgres',
        host='localhost',
        port='5432'
    )

def stats():
    conn = get_db_conn()
    cur = conn.cursor()

    # cur.execute('SELECT 1')  

    # 1) контрактников по специализации
    cur.execute("""
        SELECT cs.name, COUNT(c.contractor_id)
        FROM Contractors c
        JOIN ContractorSpecializations cs USING (specialization_id)
        GROUP BY cs.name
    """)
    for name, cnt in cur.fetchall():
        print(f"{name}: {cnt}")

    # 2) средняя цена контракта для типов клиентов
    cur.execute("""
        SELECT ct.name, AVG(co.cost)
        FROM Contracts co
        JOIN Clients cl ON co.client_id = cl.client_id
        JOIN ClientTypes ct ON cl.client_type_id = ct.client_type_id
        GROUP BY ct.name
    """)
    for name, avg_cost in cur.fetchall():
        print(f"{name}: {avg_cost:.2f}")

    # 3) операций в локации
    cur.execute("""
        SELECT ol.name, COUNT(*)
        FROM Operations o
        JOIN OperationLocations ol ON o.location_id = ol.location_id
        GROUP BY ol.name
    """)
    for loc, cnt in cur.fetchall():
        print(f"{loc}: {cnt}")

    cur.close()
    conn.close()

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = parse_qs(self.path[2:])
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """
        <html><body>
        <h1>Добавить клиента</h1>
        <form method="post" action="/add_client">
          Название: <input name="name"><br>
          Тип (ID): <input name="type_id"><br>
          Контакты: <input name="contact"><br>
          <input type="submit">
        </form>
        </body></html>
        """
        self.wfile.write(html.encode())

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = parse_qs(self.rfile.read(length).decode())
        if self.path == '/add_client':
            conn = get_db_conn()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Clients (name, client_type_id, contact_info) VALUES (%s, %s, %s)",
                (data.get('name', [''])[0],
                 data.get('type_id', [''])[0],
                 data.get('contact', [''])[0])
            )
            conn.commit()
            cur.close()
            conn.close()
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

def export_xml():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Licenses")
    root = ET.Element('Licenses')
    cols = [d[0] for d in cur.description]
    for row in cur.fetchall():
        lic = ET.SubElement(root, 'License')
        for col, val in zip(cols, row):
            el = ET.SubElement(lic, col)
            el.text = str(val)
    tree = ET.ElementTree(root)
    tree.write('licenses.xml', encoding='utf-8', xml_declaration=True)
    cur.close()
    conn.close()

def import_json():
    # old_json = 'licenses_old.json'  
    with open('licenses_export.json', encoding='utf-8') as f:
        data = json.load(f)
    conn = get_db_conn()
    cur = conn.cursor()
    for item in data:
        cur.execute(
            "INSERT INTO Licenses (issue_date, license_type_id, expiry_date, license_status_id, contract_id) "
            "VALUES (%s, %s, %s, %s, %s)",
            (item['issue_date'], item['license_type_id'],
             item['expiry_date'], item['license_status_id'],
             item.get('contract_id'))
        )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    stats()
    export_xml()
    # import_json() 
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    server.serve_forever()
