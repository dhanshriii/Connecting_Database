# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:36:42 2023

@author: Lenovo
"""

import psycopg2 as pg2
# creating connection with postgresql
#'password' is whatever paswrod you set ,we set the password in the install window
conn = pg2.connect(database = 'DVD_rental',user = 'postgres',password = 'root') 
# host and port are optional if not written then also we get the connection
 
# extablish connection and start the cursur to be ready to query
cur = conn.cursor()

# pass the PostgreSQL query as a string in execut()
cur.execute("select * from payment")

#return tuple of the first row as python objects
cur.fetchone()

#return many or N rows 
cur.fetchmany(10)

#return all rows at once
cur.fetchall()

# to save and index results,asssign it to a variable
dada = cur.fetchmany(10)

#Dont forget to close the connection 
#killing the kernel or shutting down jupyter will also close it
conn.close()


