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
    cur.execute("SELECT name, birth, death FROM archs WHERE id = ?", (id,))
    rec = cur.fetchone()
    con.close()
    if not rec:
        print("Content-Type: text/html;charset=utf-8\n")
        print("<html><body>Архитектор не найден. <a href='/cgi-bin/view_data.py'>Назад</a></body></html>")
        sys.exit()
    name, birth, death = rec
    print("Content-Type: text/html;charset=utf-8\n")
    print(f"""
    <html><head><meta charset='utf-8'><title>Редактировать архитектора</title><link rel='stylesheet' href='/style.css'></head>
    <body><div class='container'>
    <h1>Редактировать архитектора</h1>
    <form method='post' action='/cgi-bin/edit_arch.py'>
        <input type='hidden' name='id' value='{id}'>
        <label>Имя:</label><input type='text' name='name' value='{name}' required><br>
        <label>Год рождения:</label><input type='number' name='birth' value='{birth}' required><br>
        <label>Год смерти:</label><input type='number' name='death' value='{death}'><br>
        <input type='submit' value='Сохранить'>
    </form>
    <p><a href='/cgi-bin/view_data.py'>Назад</a></p>
    </div></body></html>
    """)
else:
    id = fs.getvalue("id")
    name = fs.getvalue("name")
    birth = fs.getvalue("birth")
    death = fs.getvalue("death")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("UPDATE archs SET name = ?, birth = ?, death = ? WHERE id = ?", (name, birth, death, id))
    con.commit()
    con.close()
    print("Content-Type: text/html;charset=utf-8\n")
    print("<html><body><p>Архитектор обновлён.</p><a href='/cgi-bin/view_data.py'>Назад</a></body></html>")
