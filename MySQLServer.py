import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store"
        )
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def main():
    try:
        connection = mysql.connector.connect(
            user='your_username', 
            password='your_password',
            host='your_host',
            port='your_port'
        )
        cursor = connection.cursor()
        create_database(cursor)

    except mysql.connector.Error as err:
        if err.error_num == errorcode.ER_ACCESS_DENIED_ERROR:
            print("access denied")
        elif err.error_num == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()