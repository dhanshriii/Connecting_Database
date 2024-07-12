# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:19:36 2023

@author: Lenovo
"""

import psycopg2 as pg2

#create connection
conn = pg2.connect(database = 'Testme',user = 'postgres',password = 'root')

#start cursor()
cur = conn.cursor()

# exeute and create table course admin
cur.execute("""Create table course_admin(
    course_id serial,
    course_duration VARCHAR(20) not null,
    course_fees VARCHAR(10) not null
    )""")
 
conn.commit()

cur.execute("INSERT INTO course_admin(course_duration,course_fees) values('30days',60000)")
cur.execute("INSERT INTO course_admin(course_duration,course_fees) values('40days',80000)")
cur.execute("INSERT INTO course_admin(course_duration,course_fees) values('45days',70000)")
cur.execute("INSERT INTO course_admin(course_duration,course_fees) values('30days',62000)")
cur.execute("INSERT INTO course_admin(course_duration,course_fees) values('50days',34000)")
conn.commit() 

cur.execute("""Select * from course_admin
            inner join coures1
            on coures1.course_id = course_admin.course_id
            """)
            
conn.commit()
rows = cur.fetchall()
for row in rows:
    print(row)