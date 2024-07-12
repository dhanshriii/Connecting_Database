# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:11:24 2023

@author: Lenovo
"""

import psycopg2 as pg2

#establish connection
conn = pg2.connect(database = 'Testme',user = 'postgres',password = 'root')

#start cursor()
cur = conn.cursor()

#execute order by
cur.execute("SELECT * FROM coures1 ORDER BY course_instructor")

#Make changes in the database
conn.commit()
rows = cur.fetchall()
for row in rows:
    print(row)