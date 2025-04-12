#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')


print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
n = fs.getvalue("name")
l = fs.getvalue("loc")
y = fs.getvalue("year")
sid = fs.getvalue("style_id")
aid = fs.getvalue("arch_id")
f = fs.getvalue("floors")
con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("INSERT INTO builds (name, loc, year, style_id, arch_id, floors) VALUES (?, ?, ?, ?, ?, ?)", (n, l, y, sid, aid, f))
con.commit()
con.close()
#print("Комментариев хватило бы для целой книги")
print("<html><body>Здание добавлено. <a href='/forms.html'>Вернуться</a></body></html>")
