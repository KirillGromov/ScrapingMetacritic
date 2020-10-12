from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import log

def connect():
    '''Подключение к БД'''

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            log.logging.info(f'connection established.')
        else:
            log.logging.error(f'connection failed.')

    except Error as error:
        log.logging.error(f'{error}')

    finally:
        conn.close()
        log.logging.info(f'Connection closed.')



def insert_film(name, picture, date, score, mppa):

    '''Вставка фильма'''

    query = "INSERT INTO film(name, picture, date, score, mppa) VALUES(%s,%s,%s,%s,%s)"
    args = (name, picture, date, score, mppa)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            pass
        else:
            log.logging.error(f'last insert id not found')

        conn.commit()
    except Error as error:
        log.logging.error(f'{error}')
        
    
    finally:
        cursor.close()
        conn.close()


def query_last_film():

    '''Запрос последнего записанного фильма (для лог-отчёта)'''

    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM film ORDER BY id DESC LIMIT 0,1")

        row = cursor.fetchone()

        while row is not None:
            last_film = row[0]
            row = cursor.fetchone()

    except Error as e:
        log.logging.error(f'{e}')

    finally:
        cursor.close()
        conn.close()

    return last_film
