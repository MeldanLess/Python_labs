#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, sqlite3, cgitb, datetime
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html;charset=utf-8")
print()

html_parts = []
html_parts.append("<html><head><meta charset='utf-8'><title>Просмотр записей</title>")
html_parts.append("<link rel='stylesheet' type='text/css' href='/style.css'>")
html_parts.append("<style>.new { background-color: #f2f2a0; }</style>")
html_parts.append("</head><body>")
html_parts.append("<div class='container'><h1>Все записи</h1>")

db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"
con = sqlite3.connect(db)
cur = con.cursor()
now = datetime.datetime.now()
delta = datetime.timedelta(hours=1)

# Стили
cur.execute("SELECT id, name, descr, added FROM styles")
styles = cur.fetchall()
html_parts.append("<h2>Стили</h2>")
if styles:
    html_parts.append("<table><tr><th>ID</th><th>Название</th><th>Описание</th><th>Добавлено</th><th>Действия</th></tr>")
    for s in styles:
        try:
            added_dt = datetime.datetime.strptime(s[3], "%Y-%m-%d %H:%M:%S")
        except Exception:
            added_dt = now - delta - delta
        css_class = "new" if now - added_dt < delta else ""
        html_parts.append("<tr class='%s'><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (css_class, s[0], s[1], s[2], s[3]))
        html_parts.append("<td><a href='/cgi-bin/edit_style.py?id=%s'>Редактировать</a> | <a href='/cgi-bin/delete.py?table=styles&id=%s'>Удалить</a></td></tr>" % (s[0], s[0]))
    html_parts.append("</table>")
else:
    html_parts.append("<p>Нет данных по стилям.</p>")
    
# Архитекторы
cur.execute("SELECT id, name, birth, death, added FROM archs")
archs = cur.fetchall()
html_parts.append("<h2>Архитекторы</h2>")
if archs:
    html_parts.append("<table><tr><th>ID</th><th>Имя</th><th>Год рождения</th><th>Год смерти</th><th>Добавлено</th><th>Действия</th></tr>")
    for a in archs:
        try:
            added_dt = datetime.datetime.strptime(a[4], "%Y-%m-%d %H:%M:%S")
        except Exception:
            added_dt = now - delta - delta
        css_class = "new" if now - added_dt < delta else ""
        html_parts.append("<tr class='%s'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (css_class, a[0], a[1], a[2], a[3], a[4]))
        html_parts.append("<td><a href='/cgi-bin/edit_arch.py?id=%s'>Редактировать</a> | <a href='/cgi-bin/delete.py?table=archs&id=%s'>Удалить</a></td></tr>" % (a[0], a[0]))
    html_parts.append("</table>")
else:
    html_parts.append("<p>Нет данных по архитекторам.</p>")

# Здания
cur.execute("SELECT id, name, loc, year, style_id, arch_id, floors, added FROM builds")
builds = cur.fetchall()
html_parts.append("<h2>Здания</h2>")
if builds:
    html_parts.append("<table><tr><th>ID</th><th>Название</th><th>Локация</th><th>Год</th><th>ID стиля</th><th>ID архитектора</th><th>Этажность</th><th>Добавлено</th><th>Действия</th></tr>")
    for b in builds:
        try:
            added_dt = datetime.datetime.strptime(b[7], "%Y-%m-%d %H:%M:%S")
        except Exception:
            added_dt = now - delta - delta
        css_class = "new" if now - added_dt < delta else ""
        html_parts.append("<tr class='%s'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (css_class, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]))
        html_parts.append("<td><a href='/cgi-bin/edit_build.py?id=%s'>Редактировать</a> | <a href='/cgi-bin/delete.py?table=builds&id=%s'>Удалить</a></td></tr>" % (b[0], b[0]))
    html_parts.append("</table>")
else:
    html_parts.append("<p>Нет данных по зданиям.</p>")

con.close()
html_parts.append("<p><a href='/forms.html'>Вернуться на главную</a></p>")
html_parts.append("</div></body></html>")
print("\n".join(html_parts))
