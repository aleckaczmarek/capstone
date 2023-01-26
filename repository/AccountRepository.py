from util.DBConnect import DBConnect
from model.Account import Account
import psycopg2


class AccountRepository():
    
    def insert(self, account: Account):
        dbcon = DBConnect()
        try:
            sql = """INSERT INTO account (accountnumber, customerid, currentbalance)
             VALUES(%s, %s, %s) RETURNING id;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (account.account_number, account.customer_id, account.current_balance))
            id = cursor.fetchone()[0]
            dbcon.setCommit()
            cursor.close()
            return id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
     
    def update(self, account: Account):
        dbcon = DBConnect()
        try:
            sql = """UPDATE account SET accountnumber = %s, customerid = %s, currentbalance = %s WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (account.account_number, account.customer_id, account.current_balance, account.id))
            dbcon.setCommit()
            cursor.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
    
    def getAll(self):
        dbcon = DBConnect()
        accounts = []
        try:
            sql = """SELECT * from account;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, ())
            data = cursor.fetchall()
            for account in data:
                accounts.append(Account(account[0],account[1],account[2],account[3]))
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None
        finally:
            return accounts

    def get(self, id):
        dbcon = DBConnect()
        account = None
        try:
            sql = """SELECT * from account WHERE id = %s;"""
            cursor = dbcon.getCursor()
            cursor.execute(sql, (str(id),))
            data = cursor.fetchall()
            account = Account(data[0][0],data[0][1],data[0][2],data[0][3])
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return account
        finally:
            return account

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
