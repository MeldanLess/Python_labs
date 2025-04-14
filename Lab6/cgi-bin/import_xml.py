#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgitb, sqlite3
from xml.dom.minidom import parse
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html;charset=utf-8")
print()

# Парсим XML-файл
dom = parse("buildings.xml")
blds = dom.getElementsByTagName("building")

# Подключаемся к базе данных и вставляем данные из XML в таблицу builds
con = sqlite3.connect("architecture.db")
cur = con.cursor()
for b in blds:
    nm = b.getElementsByTagName("name")[0].firstChild.data
    lc = b.getElementsByTagName("loc")[0].firstChild.data
    yr = int(b.getElementsByTagName("year")[0].firstChild.data)
    sid = int(b.getElementsByTagName("style_id")[0].firstChild.data)
    aid = int(b.getElementsByTagName("arch_id")[0].firstChild.data)
    fl = int(b.getElementsByTagName("floors")[0].firstChild.data)
    cur.execute("INSERT INTO builds (name, loc, year, style_id, arch_id, floors) VALUES (?, ?, ?, ?, ?, ?)",
                (nm, lc, yr, sid, aid, fl))
con.commit()
con.close()

# Выводим результат в браузер
print("<html><head><meta charset='utf-8'><title>Импорт XML</title>")
print("<link rel='stylesheet' type='text/css' href='/style.css'>")
print("</head><body>")
print("<div class='container'><h1>Импорт XML</h1>")
print("<p>Импорт из XML завершён!</p>")
print("<p><a href='/forms.html'>Вернуться на главную страницу</a></p>")
print("</div></body></html>")
