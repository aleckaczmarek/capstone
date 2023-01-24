from util.DBConnect import DBConnect
from model.Account import Account
import psycopg2


class AccountRepository():
    
    def insert(self, account: Account):
        dbcon = DBConnect()
        try:
            sql = """INSERT INTO account (accountnumber, customerid, currentbalance)
             VALUES(%s, %s, %s);"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (account.account_number, account.customer_id, account.current_balance))
            dbcon.setCommit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            dbcon.closeConnection()
     
    def update(self, account: Account):
        dbcon = DBConnect()
        try:
            sql = """UPDATE account SET accountnumber = %s, customerid = %s, currentbalance = %s WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (account.account_number, account.customer_id, account.current_balance, account.id))
            dbcon.setCommit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            dbcon.closeConnection()
     
    def delete(self, account: Account):
        dbcon = DBConnect()
        try:
            sql = """DELETE FROM account WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(account.id),))
            dbcon.setCommit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            dbcon.closeConnection()
