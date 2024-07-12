# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:20:46 2023

@author: Lenovo
"""

import psycopg2 as pg2

#connecting python with postgreSQL
conn = pg2.connect(database = 'Testme',user = 'postgres',password = 'root')

#establish connection and start cursur to be ready to query
cur = conn.cursor()

#execute command and create courses table
cur.execute("""Create table coures1(
    course_id serial primary key,
    course_name varchar(50) unique not null,
    course_instructor varchar (100) not null,
    topic varchar(20) not null);"""
)

#make changes to database persistent
conn.commit() #We created a table named coures1 in the database 
#and it is visible in postgreSQL

#close cursur communication with database
cur.close()


















