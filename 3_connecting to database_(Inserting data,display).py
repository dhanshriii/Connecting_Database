# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 08:24:15 2023

@author: Lenovo
"""

import psycopg2 as pg2
##Inserting to postgresql database using python
#create connection with postgreSQL
conn = pg2.connect(database = 'Testme',password = 'root',user = 'postgres')

#start the cursor
cur = conn.cursor()

#execute command and insert in the table
cur.execute("INSERT INTO coures1 (course_name,course_instructor,topic) values('Introduction to SQL','Ram','Julia')");
cur.execute("INSERT INTO coures1 (course_name,course_instructor,topic) values('Analysing survey data in python','sham','Python')")
cur.execute("INSERT INTO coures1 (course_name,course_instructor,topic) values('Intoduction to chatgpt','anesh','theory')")
cur.execute("INSERT INTO coures1 (course_name,course_instructor,topic) values('introduction to statistics in R','jayesh','R')")
cur.execute("INSERT INTO coures1 (course_name,course_instructor,topic) values('Hypothesis testing in python','ramesh','Pthon')")

conn.commit()
cur.close()
conn.close()

############################################################

import psycopg2 as pg2

#create connection
conn = pg2.connect(database = 'Testme',user = 'postgres',password = 'root')

#start cusrsor()
cur = conn.cursor()

#execute query
cur.execute("SELECT * from coures1")
rows = cur.fetchall()
conn.commit()

conn.close()

for row in rows:
    print(row)
    

