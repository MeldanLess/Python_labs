#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

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
#print("Some old comment")
print("<html><head><meta charset='utf-8'><title>Результат</title></head><body>")
print("Стиль добавлен. <a href='/forms.html'>Вернуться</a>")
print("</body></html>")
