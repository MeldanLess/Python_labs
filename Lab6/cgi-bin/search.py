#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
query = fs.getvalue("q", "").strip()

html = []
html.append("<html><head><meta charset='utf-8'><title>Результаты поиска</title>")
html.append("<link rel='stylesheet' type='text/css' href='/style.css'>")
html.append("</head><body>")
html.append("<div class='container'>")
html.append("<h1>Результаты поиска</h1>")
html.append("<p>По запросу: <strong>%s</strong></p>" % query)

if not query:
    html.append("<p>Пустой поисковый запрос.</p>")
else:
    # Подключение к базе данных
    con = sqlite3.connect("D:/1_Univer/Python/Python_labs/Lab6/architecture.db")
    cur = con.cursor()

    # Выполняем поиск в таблицах buildings, styles и archs
    like_query = "%" + query + "%"
    cur.execute("""
       SELECT 'Здание', name, loc, year 
       FROM builds 
       WHERE name LIKE ?
    """, (like_query,))
    buildings = cur.fetchall()

    cur.execute("""
       SELECT 'Стиль', name, descr 
       FROM styles 
       WHERE name LIKE ? OR descr LIKE ?
    """, (like_query, like_query))
    styles = cur.fetchall()

    cur.execute("""
       SELECT 'Архитектор', name, birth, death 
       FROM archs 
       WHERE name LIKE ?
    """, (like_query,))
    archs = cur.fetchall()

    con.close()

    if not (buildings or styles or archs):
        html.append("<p>Ничего не найдено.</p>")
    else:
        # Вывод результатов поиска
        if buildings:
            html.append("<h2>Здания</h2>")
            html.append("<table>")
            html.append("<tr><th>Название</th><th>Локация</th><th>Год</th></tr>")
            for r in buildings:
                html.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (r[1], r[2], r[3]))
            html.append("</table>")
        if styles:
            html.append("<h2>Стили</h2>")
            html.append("<table>")
            html.append("<tr><th>Название</th><th>Описание</th></tr>")
            for r in styles:
                html.append("<tr><td>%s</td><td>%s</td></tr>" % (r[1], r[2]))
            html.append("</table>")
        if archs:
            html.append("<h2>Архитекторы</h2>")
            html.append("<table>")
            html.append("<tr><th>Имя</th><th>Год рождения</th><th>Год смерти</th></tr>")
            for r in archs:
                html.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (r[1], r[2], r[3]))
            html.append("</table>")

html.append("<p><a href='/forms.html'>Вернуться на главную</a></p>")
html.append("</div></body></html>")

print("\n".join(html))
