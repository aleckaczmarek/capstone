from pickle import TRUE
from model.Address import Address
from model.Customer import Customer
from repository.AccountRepository import AccountRepository
from repository.AddressRepository import AddressRepository
from repository.CustomerRepository import CustomerRepository
from model.Account import Account
from random import randint
import psycopg2
# x Open a new account
# x Retrieve information on all accounts
# x Retrieve information for a specific account
# x Execute a withdrawal from an existing account
# x Execute a deposit to an existing account
# x Close an existing account
class AccountService():
    repo = AccountRepository()
    
    def createAccount(self,amount: float,id):
        repoAddress = AddressRepository()
        repoCustomer = CustomerRepository()
        try:
            customer:Customer = repoCustomer.get(id)
            if type(customer) != Customer and amount >= 25:
                addressId = repoAddress.insert(Address(None,"BaseCity", "BaseState", "BeZip","BaseStreet"))
                cid = repoCustomer.insert(Customer(None,"NewCust","NewCust",addressId, "baseemail@email.com"))
                self.repo.insert(Account(None,(str(randint(10000, 99999))),cid, amount ))
                return True
            elif amount >= 25:
                acct = Account(None,(str(randint(10000, 99999))),id, amount )
                print(acct)
                self.repo.insert(acct)
                return True
            else:
                return False
        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR CREATING ",error)
            return False

    def getAccounts(self):
        accounts = False
        try:
            accounts = self.repo.getAll()
            return accounts
        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR GETTING ",error)
            return accounts
            

    def getAccount(self,id):
        account = False
        try:
            account = self.repo.get(id)
            return account
        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR GETTING ",error)
            return account 

    def withdrawal(self, amount: float, id):
        try:
            account: Account = self.getAccount(id)
            newBalance = account.current_balance - abs(amount)
            if newBalance > 0 and amount > 0:
                account.updateBalance(newBalance)
                self.repo.update(account)
                return True
            else:
                return False
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False

    def deposit(self, amount: float, id):
        try:
            account: Account = self.getAccount(id)
            newBalance = account.current_balance + abs(amount)
            if newBalance > 0 and amount > 0:
                account.updateBalance(newBalance)
                self.repo.update(account)
                return True
            else:
                return False
        except (Exception, psycopg2.DatabaseError) as error:
            return False

    def closeAccount(self,id):
        repoAddress = AddressRepository()
        repoCustomer = CustomerRepository()
        try:
            account:Account = self.repo.get(id)
            customer:Customer = repoCustomer.get(account.customer_id)
            address:Address = repoAddress.get(customer.address_id)
            self.repo.delete(account)
            repoCustomer.delete(customer)
            repoAddress.delete(address)
            return True

        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR CREATING ",error)
            return False
