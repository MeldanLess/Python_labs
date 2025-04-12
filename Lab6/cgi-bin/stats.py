#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-Type: text/html;charset=utf-8")
print()

con = sqlite3.connect("architecture.db")
cur = con.cursor()

# Запрос 1: Количество зданий по каждому стилю
cur.execute("""
    SELECT styles.name, COUNT(builds.id)
    FROM builds
    JOIN styles ON builds.style_id = styles.id
    GROUP BY styles.name
""")
q1 = cur.fetchall()

# Запрос 2: Среднее количество этажей по каждому стилю
cur.execute("""
    SELECT styles.name, AVG(builds.floors)
    FROM builds
    JOIN styles ON builds.style_id = styles.id
    GROUP BY styles.name
""")
q2 = cur.fetchall()

# Запрос 3: Количество зданий для каждого архитектора
cur.execute("""
    SELECT archs.name, COUNT(builds.id)
    FROM builds
    JOIN archs ON builds.arch_id = archs.id
    GROUP BY archs.name
""")
q3 = cur.fetchall()

con.close()

print("<html><head><meta charset='utf-8'><title>Статистика</title></head><body>")
print("<h1>Статистические запросы</h1>")

print("<h2>Здания по стилям</h2>")
print("<table border='1'><tr><th>Стиль</th><th>Кол-во зданий</th></tr>")
for r in q1:
    print("<tr><td>%s</td><td>%s</td></tr>" % r)
print("</table>")

print("<h2>Среднее этажность по стилям</h2>")
print("<table border='1'><tr><th>Стиль</th><th>Среднее этажей</th></tr>")
for r in q2:
    print("<tr><td>%s</td><td>%s</td></tr>" % r)
print("</table>")

print("<h2>Здания по архитекторам</h2>")
print("<table border='1'><tr><th>Архитектор</th><th>Кол-во зданий</th></tr>")
for r in q3:
    print("<tr><td>%s</td><td>%s</td></tr>" % r)
print("</table>")

print("</body></html>")
