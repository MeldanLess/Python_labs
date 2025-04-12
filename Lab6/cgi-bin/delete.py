#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
table = fs.getvalue("table")
record_id = fs.getvalue("id")
if not table or not record_id:
    print("<html><body>Некорректные параметры. <a href='/forms.html'>Return</a></body></html>")
    sys.exit()

if table not in ["styles", "archs", "builds"]:
    print("<html><body>Неверная таблица. <a href='/forms.html'>Return</a></body></html>")
    sys.exit()

db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"
con = sqlite3.connect(db)
cur = con.cursor()
try:
    cur.execute("DELETE FROM %s WHERE id = ?" % table, (record_id,))
    con.commit()
    msg = "Запись удалена"
except Exception as e:
    msg = "Ошибка: " + str(e)
con.close()
print("<html><head><meta charset='utf-8'><title>Удаление</title></head><body>")
print("<p>%s</p>" % msg)
print("<p><a href='/cgi-bin/view_data.py'>Вернуться к записям</a></p>")
print("</body></html>")
