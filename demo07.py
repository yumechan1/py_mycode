dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123",
    "database": "sql_study"
}

import mysql.connector
from pprint import pprint
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

cursor.execute("""
    select * from students
""")

pprint(cursor.fetchall())
cursor.execute("""
    insert into students(name,age)
    values
    (
        "大华",
        18
    )
""")
# print(cursor.fetchall())
cursor.execute("""
    select * from students
""")

pprint(cursor.fetchall())
cursor.close()
conn.clost()