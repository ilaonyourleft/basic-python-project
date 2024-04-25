from connection.postgresql_connection import connect_to_db as postgresql_connect
from connection.mysql_connection import connect_to_db as mysql_connect


def execute_query(conn, query):
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute a SQL query
    cur.execute(query)

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Close the cursor
    cur.close()

    return rows


def main():
    # Connect to the database

    # PostgreSQL
    # conn = postgresql_connect()

    # MySQL
    conn = mysql_connect()

    # Execute a query
    query = "show tables;"
    rows = execute_query(conn, query)

    # Print the rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
