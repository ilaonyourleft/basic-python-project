import configparser
import psycopg2


def connect_to_db():
    # Load the connection parameters from the .ini file
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    db_params = {
        'host': config.get('postgresql_db', 'host'),
        'port': config.get('postgresql_db', 'port'),
        'database': config.get('postgresql_db', 'database'),
        'user': config.get('postgresql_db', 'user'),
        'password': config.get('postgresql_db', 'password')
    }

    # Establish a connection to the database
    conn = psycopg2.connect(**db_params)
    return conn
