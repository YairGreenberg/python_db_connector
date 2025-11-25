import mysql.connector
from connector_sql import connected



def get_connection():
    connected= mysql.connector.connect(
        host='127.0.0.1',
        user= 'root',
        password='',
        database='classicmodels'
    )
    if connected.is_connected():
        print("connected to mysql database successfully! ")
        return connected
    else:
        return "your sql not connected:"

def create_table():
    my_cursor=connected.cursor()
    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS courses ("
                               #"id INT AUTO_INCREMENT PRIMARY KEY,"
        "institution VARCHAR(255) NOT NULL,"
        "city VARCHAR(255) NOT NULL,"
        "address VARCHAR(255),"
        "course VARCHAR(255) NOT NULL,"
        "district VARCHAR(255),"
        "telephone VARCHAR(255),"
        "email VARCHAR(255));"
    )

