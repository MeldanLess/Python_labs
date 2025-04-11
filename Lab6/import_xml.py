#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from xml.dom.minidom import parse

dom = parse("buildings.xml")
blds = dom.getElementsByTagName("building")

con = sqlite3.connect("architecture.db")
cur = con.cursor()
for b in blds:
    nm = b.getElementsByTagName("name")[0].firstChild.data
    lc = b.getElementsByTagName("loc")[0].firstChild.data
    yr = int(b.getElementsByTagName("year")[0].firstChild.data)
    sid = int(b.getElementsByTagName("style_id")[0].firstChild.data)
    aid = int(b.getElementsByTagName("arch_id")[0].firstChild.data)
    fl = int(b.getElementsByTagName("floors")[0].firstChild.data)
    cur.execute("INSERT INTO builds (name, loc, year, style_id, arch_id, floors) VALUES (?, ?, ?, ?, ?, ?)",
                (nm, lc, yr, sid, aid, fl))
con.commit()
con.close()
print("Import completed!")
