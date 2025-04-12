#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgi, cgitb, sqlite3
import datetime
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

fs = cgi.FieldStorage()
db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"

if fs.getvalue("id") and not fs.getvalue("name"):
    record_id = fs.getvalue("id")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT name, descr FROM styles WHERE id = ?", (record_id,))
    rec = cur.fetchone()
    con.close()
    if rec is None:
        print("Content-Type: text/html;charset=utf-8")
        print()
        print("<html><body>Запись не найдена. <a href='/cgi-bin/view_data.py'>Return</a></body></html>")
        sys.exit()
    style_name, style_descr = rec
    print("Content-Type: text/html;charset=utf-8")
    print()
    print("<html><head><meta charset='utf-8'><title>Редактировать стиль</title><link rel='stylesheet' type='text/css' href='/style.css'></head><body>")
    print("<div class='container'><h1>Редактировать стиль</h1>")
    print("<form method='post' action='/cgi-bin/edit_style.py'>")
    print("<input type='hidden' name='id' value='%s'>" % record_id)
    print("<label>Название стиля:</label>")
    print("<input type='text' name='name' value='%s' required>" % style_name)
    print("<label>Описание стиля:</label>")
    print("<textarea name='descr' rows='3' required>%s</textarea>" % style_descr)
    print("<input type='submit' value='Сохранить'>")
    print("</form>")
    print("<p><a href='/cgi-bin/view_data.py'>Return</a></p></div></body></html>")
else:
    record_id = fs.getvalue("id")
    new_name = fs.getvalue("name")
    new_descr = fs.getvalue("descr")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("UPDATE styles SET name = ?, descr = ? WHERE id = ?", (new_name, new_descr, record_id))
    con.commit()
    con.close()
    print("Content-Type: text/html;charset=utf-8")
    print()
    print("<html><head><meta charset='utf-8'><title>Редактировать стиль</title></head><body>")
    print("<p>Стиль обновлен. <a href='/cgi-bin/view_data.py'>Return</a></p>")
    print("</body></html>")
