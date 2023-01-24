import psycopg2
class DBConnect():
    conn = psycopg2.connect(database="db01",
                        host="localhost",
                        user="postgres",
                        password="password123",
                        port="5432")

    def getCursor(self):
        cursor = self.conn.cursor()
        return cursor

    def setCommit(self):
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()