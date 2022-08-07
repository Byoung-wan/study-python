import sqlite3 as sql

conn = sql.connect("d:/pyproject/test/sql/customer.db", isolation_level=None)
cur = conn.cursor()

upd_sql = "UPDATE customer_data SET email='0000000000' WHERE id=100"
cur.execute(upd_sql)
conn.commit()

query = "SELECT * FROM customer_data"
cur.execute(query)
rows = cur.fetchall()
for r in rows[:100]:
    print(r)