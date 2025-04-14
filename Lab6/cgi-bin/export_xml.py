#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgitb, sqlite3
from xml.dom.minidom import Document
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html;charset=utf-8")
print()

# Подключаемся к базе данных и получаем данные из таблицы builds
con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("SELECT name, loc, year, style_id, arch_id, floors FROM builds")
data = cur.fetchall()
con.close()

# Создаем XML-документ
doc = Document()
root = doc.createElement("buildings")
doc.appendChild(root)
for rec in data:
    b = doc.createElement("building")
    for info, tag in zip(rec, ["name", "loc", "year", "style_id", "arch_id", "floors"]):
        e = doc.createElement(tag)
        t = doc.createTextNode(str(info))
        e.appendChild(t)
        b.appendChild(e)
    root.appendChild(b)

# Сохраняем XML в файл
with open("buildings.xml", "w", encoding="utf-8") as f:
    f.write(doc.toprettyxml(indent="  "))

# Выводим результат в браузер
print("<html><head><meta charset='utf-8'><title>Экспорт XML</title>")
print("<link rel='stylesheet' type='text/css' href='/style.css'>")
print("</head><body>")
print("<div class='container'><h1>Экспорт XML</h1>")
print("<p>Экспорт в XML завершён! Файл <strong>buildings.xml</strong> обновлен.</p>")
print("<p><a href='/forms.html'>Вернуться на главную страницу</a></p>")
print("</div></body></html>")
