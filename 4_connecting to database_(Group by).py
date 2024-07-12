# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:02:46 2023

@author: Lenovo
"""

import psycopg2 as pg2

#create connection with postgresql
conn = pg2.connect(database = 'Testme',user = 'postgres',password = 'root')

#start cursor
cur = conn.cursor()

#execute group by
cur.execute('SELECT course_instructor,COUNT(*) FROM coures1 GROUP BY course_instructor')

#make the changes in data persistently
conn.commit()
