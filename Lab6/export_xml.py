#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from xml.dom.minidom import Document

con = sqlite3.connect("architecture.db")
cur = con.cursor()
cur.execute("SELECT name, loc, year, style_id, arch_id, floors FROM builds")
data = cur.fetchall()
con.close()

doc = Document()
root = doc.createElement("buildings")
doc.appendChild(root)
for rec in data:
    b = doc.createElement("building")
    for info, tag in zip(rec, ["name", "loc", "year", "style_id", "arch_id", "floors"]):
        e = doc.createElement(tag)
        t = doc.createTextNode(str(info))
        e.appendChild(t)
        b.appendChild(e)
    root.appendChild(b)

with open("buildings.xml", "w", encoding="utf-8") as f:
    f.write(doc.toprettyxml(indent="  "))

print("Export completed!")
