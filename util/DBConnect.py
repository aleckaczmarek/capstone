import psycopg2

conn = psycopg2.connect(database="db01",
                        host="localhost",
                        user="postgres",
                        password="password123",
                        port="5432")

cursor = conn.cursor()

def getCursor():
    return cursor

# cursor.query("INSERT " FROM example_table")
