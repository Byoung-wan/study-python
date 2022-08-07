import sqlite3 as sql
import string
import random

#DB file generation and connect (연결자=conn)
conn = sql.connect("d:/pyproject/test/sql/customer.db", isolation_level=None)

#cursor connect
cur = conn.cursor()

#Table generation SQL and execution
crt_sql = """CREATE TABLE IF NOT EXISTS customer_data(
    id integer primary key autoincrement, 
    username varchar(200) not null, 
    email text default "")"""

cur.execute(crt_sql)
conn.commit()