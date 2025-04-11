#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, cgi, cgitb
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("""
    SELECT b.name, b.loc, b.year, s.name, a.name, b.floors 
    FROM builds b 
    LEFT JOIN styles s ON b.style_id = s.id 
    LEFT JOIN archs a ON b.arch_id = a.id
""")
rows = cur.fetchall()
con.close()

print("<html><head><meta charset='utf-8'><title>Здания</title></head><body>")
print("<h1>Список зданий</h1>")
print("<table border='1'><tr><th>Название</th><th>Локация</th><th>Год</th><th>Стиль</th><th>Архитектор</th><th>Этажность</th></tr>")
for r in rows:
    print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % r)
print("</table>")
print("</body></html>")
