#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi, cgitb, sqlite3
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
n = fs.getvalue("name")
d = fs.getvalue("descr")
con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("INSERT INTO styles (name, descr) VALUES (?, ?)", (n, d))
con.commit()
con.close()
#print("Было больше комментариев")
print("<html><body>Стиль добавлен. <a href='/forms.html'>Вернуться</a></body></html>")
