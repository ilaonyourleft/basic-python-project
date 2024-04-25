import configparser
import mysql.connector
from mysql.connector import Error


def connect_to_db():
    # Load the connection parameters from the .ini file
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    db_params = {
        'host': config.get('mysql_db', 'host'),
        'port': config.get('mysql_db', 'port'),
        'database': config.get('mysql_db', 'database'),
        'user': config.get('mysql_db', 'user'),
        'password': config.get('mysql_db', 'password')
    }

    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**db_params)

        if connection.is_connected():
            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)
