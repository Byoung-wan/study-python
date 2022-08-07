import sqlite3 as sql
import string
import random

#DB file generation and connect (연결자=conn)
conn = sql.connect("d:/pyproject/test/sql/customer.db", isolation_level=None)

#cursor connect
cur = conn.cursor()

# INsert SQL 명령 작성
for i in range(1000):
    ins_sql = "INSERT INTO customer_data(username , email) VALUES (?, ?);"
    rnd = "".join([random.choice(string.ascii_letters+string.digits) for i in range(10)])
    print(rnd)
    cur.execute(ins_sql, (i, rnd))
        
conn.commit()
#DB connection close
#conn.close()