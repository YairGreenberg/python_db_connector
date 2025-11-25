import mysql.connector
from mysql.connector import connect



connected = mysql.connector.connect(
        user="root",
        password="",
        host='127.0.0.1',
        database="classicmodels",
)
print("connected, server version: ",connected.get_server_info())


cursor = connected.cursor()
cursor.execute("SELECT * FROM customers")

# cursor.execute("SELECT * FROM employees with M in name") ##complit
# 29


data = cursor.fetchall()
print(data)









