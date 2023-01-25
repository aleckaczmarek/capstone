from util.DBConnect import DBConnect
from model.Customer import Customer
import psycopg2


class CustomerRepository():
    
    def insert(self, object: Customer):
        dbcon = DBConnect()
        try:
            sql = """INSERT INTO customer (firstname, lastname, addressid, email)
             VALUES(%s, %s, %s, %s) RETURNING id;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (object.first_name, object.last_name, object.address_id, object.email_address))
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
            sql = """SELECT * from customer WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(id),))
            data = cursor.fetchall()
            object = Customer(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4])
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return object
        finally:
            return object

    def delete(self, object: Customer):
        dbcon = DBConnect()
        try:
            sql = """DELETE FROM customer WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(object.id),))
            dbcon.setCommit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
