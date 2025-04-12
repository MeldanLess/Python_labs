#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, cgi, cgitb, sqlite3
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

fs = cgi.FieldStorage()
db = "D:/1_Univer/Python/Python_labs/Lab6/architecture.db"

if fs.getvalue("id") and not fs.getvalue("name"):
    id = fs.getvalue("id")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT name, loc, year, style_id, arch_id, floors FROM builds WHERE id = ?", (id,))
    rec = cur.fetchone()
    con.close()
    if not rec:
        print("Content-Type: text/html;charset=utf-8\n")
        print("<html><body>Здание не найдено. <a href='/cgi-bin/view_data.py'>Назад</a></body></html>")
        sys.exit()
    name, loc, year, style_id, arch_id, floors = rec
    print("Content-Type: text/html;charset=utf-8\n")
    print(f"""
    <html><head><meta charset='utf-8'><title>Редактировать здание</title><link rel='stylesheet' href='/style.css'></head>
    <body><div class='container'>
    <h1>Редактировать здание</h1>
    <form method='post' action='/cgi-bin/edit_build.py'>
        <input type='hidden' name='id' value='{id}'>
        <label>Название:</label><input type='text' name='name' value='{name}' required><br>
        <label>Локация:</label><input type='text' name='loc' value='{loc}' required><br>
        <label>Год постройки:</label><input type='number' name='year' value='{year}' required><br>
        <label>ID стиля:</label><input type='number' name='style_id' value='{style_id}' required><br>
        <label>ID архитектора:</label><input type='number' name='arch_id' value='{arch_id}' required><br>
        <label>Этажей:</label><input type='number' name='floors' value='{floors}' required><br>
        <input type='submit' value='Сохранить'>
    </form>
    <p><a href='/cgi-bin/view_data.py'>Назад</a></p>
    </div></body></html>
    """)
else:
    id = fs.getvalue("id")
    name = fs.getvalue("name")
    loc = fs.getvalue("loc")
    year = fs.getvalue("year")
    style_id = fs.getvalue("style_id")
    arch_id = fs.getvalue("arch_id")
    floors = fs.getvalue("floors")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("""UPDATE builds 
                   SET name=?, loc=?, year=?, style_id=?, arch_id=?, floors=? 
                   WHERE id=?""", (name, loc, year, style_id, arch_id, floors, id))
    con.commit()
    con.close()
    print("Content-Type: text/html;charset=utf-8\n")
    print("<html><body><p>Здание обновлено.</p><a href='/cgi-bin/view_data.py'>Назад</a></body></html>")
