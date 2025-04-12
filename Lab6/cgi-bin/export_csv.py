#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgi, cgitb, sqlite3, csv, io
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"
con = sqlite3.connect(db)
cur = con.cursor()
cur.execute("SELECT id, name, loc, year, style_id, arch_id, floors FROM builds")
rows = cur.fetchall()
con.close()

output = io.StringIO()
writer = csv.writer(output)
writer.writerow(["ID", "Название", "Локация", "Год", "ID стиля", "ID архитектора", "Этажность"])
for row in rows:
    writer.writerow(row)
csv_data = output.getvalue()
output.close()

print("Content-Type: text/csv;charset=utf-8")
print("Content-Disposition: attachment; filename=\"buildings.csv\"")
print()
print(csv_data)
