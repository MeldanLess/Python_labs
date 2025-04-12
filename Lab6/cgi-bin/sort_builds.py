#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
sort_by = fs.getvalue("sort_by", "year")
if sort_by not in ["name", "year", "floors"]:
    sort_by = "year"
db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"
con = sqlite3.connect(db)
cur = con.cursor()
query = "SELECT id, name, loc, year, style_id, arch_id, floors FROM builds ORDER BY " + sort_by
cur.execute(query)
builds = cur.fetchall()
con.close()

html = []
html.append("<html><head><meta charset='utf-8'><title>Сортировка зданий</title>")
html.append("<link rel='stylesheet' type='text/css' href='/style.css'>")
html.append("</head><body>")
html.append("<div class='container'><h1>Здания (сортировка по %s)</h1>" % sort_by)
html.append("<p><a href='/cgi-bin/view_data.py'>Return ко всем записям</a></p>")
html.append("<table><tr><th>ID</th><th>Название</th><th>Локация</th><th>Год</th><th>Стиль</th><th>Архитектор</th><th>Этажность</th></tr>")
for b in builds:
    html.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (b[0], b[1], b[2], b[3], b[4], b[5], b[6]))
html.append("</table>")
html.append("</div></body></html>")
print("\n".join(html))
