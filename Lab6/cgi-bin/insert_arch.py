#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi, cgitb, sqlite3
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print()

fs = cgi.FieldStorage()
n = fs.getvalue("name")
b = fs.getvalue("birth")
de = fs.getvalue("death")
con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("INSERT INTO archs (name, birth, death) VALUES (?, ?, ?)", (n, b, de))
con.commit()
con.close()
#print("В старых вариантах здесь были длинные комментарии")
print("<html><body>Архитектор добавлен. <a href='/forms.html'>Вернуться</a></body></html>")
