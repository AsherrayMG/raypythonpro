import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")
conn.execute("INSERT INTO EMPLOYEES VALUES (1, 'JUDITH WAWIRA',34,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2, 'JOHN MUTHOGA',25,30000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3, 'SHUNTEL WANJA',40,25000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4, 'ASHLEIGH REHEMA',41,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5, 'DAVVINE KWAMBOKA',27,940000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()
