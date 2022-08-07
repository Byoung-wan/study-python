import sqlite3 as sql

#DB file generation and connect (연결자=conn)
conn = sql.connect("d:/pyproject/test/sql/customer.db", isolation_level=None)
#cursor connect
cur = conn.cursor()

SELECT_SQL = "SELECT * FROM customer_data"
cur.execute(SELECT_SQL)
rows = cur.fetchall()
for r in rows:
    print(r)   

