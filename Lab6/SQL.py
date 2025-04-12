#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

def create_db():
    con = sqlite3.connect("architecture.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS styles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            descr TEXT,
            added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS archs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth INTEGER,
            death INTEGER,
            added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS builds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            loc TEXT,
            year INTEGER,
            style_id INTEGER,
            arch_id INTEGER,
            floors INTEGER,
            added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (style_id) REFERENCES styles(id),
            FOREIGN KEY (arch_id) REFERENCES archs(id)
        )
    """)
    con.commit()
    con.close()

def fill_db():
    con = sqlite3.connect("architecture.db")
    cur = con.cursor()
    styles = [
        ("Готика", "Стиль с остроконечными арками"),
        ("Модерн", "Органические формы, новые материалы"),
        ("Брутализм", "Грубые формы, бетон")
    ]
    for s in styles:
        cur.execute("INSERT INTO styles (name, descr) VALUES (?, ?)", s)
    archs = [
        ("Гауди", 1852, 1926),
        ("Райт", 1867, 1959),
        ("Ле Корбюзье", 1887, 1965)
    ]
    for a in archs:
        cur.execute("INSERT INTO archs (name, birth, death) VALUES (?, ?, ?)", a)
    builds = [
        ("Саграда Фамилия", "Барселона", 1882, 1, 1, 18),
        ("Дом Эрг", "Чикаго", 1905, 2, 2, 10),
        ("Вилла Савой", "Париж", 1931, 3, 3, 2)
    ]
    for b in builds:
        cur.execute("INSERT INTO builds (name, loc, year, style_id, arch_id, floors) VALUES (?, ?, ?, ?, ?, ?)", b)
    con.commit()
    con.close()

if __name__ == "__main__":
    create_db()
    fill_db()
    print("DB created and filled!")
