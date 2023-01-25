from util.DBConnect import DBConnect
from model.Address import Address
import psycopg2


class AddressRepository():
    def insert(self, object: Address):
        dbcon = DBConnect()
        try:
            sql = """INSERT INTO address (city, state, zipcode, street)
             VALUES(%s, %s, %s, %s) RETURNING id;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (object.city, object.state, object.zipcode, object.street))
            id = cursor.fetchone()[0]
            dbcon.setCommit()
            cursor.close()
            return id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get(self, id):
        dbcon = DBConnect()
        object = None
        try:
            sql = """SELECT * from address WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(id),))
            data = cursor.fetchall()
            object = Address(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4])
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return object
        finally:
            return object

    def delete(self, object: Address):
        dbcon = DBConnect()
        try:
            sql = """DELETE FROM address WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(object.id),))
            dbcon.setCommit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
