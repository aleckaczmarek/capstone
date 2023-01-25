from pickle import TRUE
from model.Address import Address
from model.Customer import Customer
from repository.AccountRepository import AccountRepository
from repository.AddressRepository import AddressRepository
from repository.CustomerRepository import CustomerRepository
from model.Account import Account
from random import randint
import psycopg2
# o Open a new account
# o Retrieve information on all accounts
# o Retrieve information for a specific account
# o Execute a withdrawal from an existing account
# o Execute a deposit to an existing account
# o Close an existing account
class AccountService():
    repo = AccountRepository()
    
    def createAccount(self,amount: float,id):
        repoAddress = AddressRepository()
        repoCustomer = CustomerRepository()
        try:
            #TODO add logic to check if account exists, if not create account with blank address
            customer:Customer = repoCustomer.get(id)
            if customer.id != id:
                addressId = repoAddress.insert(Address(None,"BaseCity", "BaseState", "BaseZip","BaseStreet"))
                custId = repoCustomer.insert(Customer(None,"NewCust","NewCust",addressId))
            if amount >= 25 and customer:
                self.repo.insert(Account(None,(str(randint(10000, 99999))+'-'+str(id)),id, amount ))
                return True
            else:
                return False
        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR CREATING ",error)
            return False

    def getAccounts(self):
        accounts = False
        try:
            #TODO add logic to check if account exists, if not create account with blank address
            accounts = self.repo.getAll()
            return accounts
        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR GETTING ",error)
            return accounts
            

    def getAccount(self,id):
        account = False
        try:
            #TODO add logic to check if account exists, if not create account with blank address
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
