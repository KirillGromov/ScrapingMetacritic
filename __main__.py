import mysql
import mysql.connector
from mysql.connector import Error

def connect():

    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            database='films',
            user = 'root',
            passwd = '3470',
        )

        if conn.is_connected():
            print('Connected to Films')
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    connect()



