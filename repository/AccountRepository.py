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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            dbcon.closeConnection()
     
    # def update(self, account: Account):
    #     try:
    #         sql = """INSERT INTO account(id, accountnumber, customerid, currentbalance)
    #          VALUES(%s, %s, %s, %s) RETURNING id;"""
    #         cursor = getCursor()
    #         cursor.execute(sql, (account.id, account.account_number, account.customer_id, account.current_balance))
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         closeConnection()
