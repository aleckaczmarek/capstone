import uvicorn
from fastapi import FastAPI
from service.AccountService import AccountService
from model.Account import Account
from typing import List
# x Open a new account
# x Retrieve information on all accounts
# x Retrieve information for a specific account
# x Execute a withdrawal from an existing account
# x Execute a deposit to an existing account
# x Close an existing account       
app = FastAPI()
service = AccountService()
    
@app.get('/api/accounts', response_model=List[Account])
async def retrieve_accounts():
    return service.getAccounts()

@app.get('/api/account/{id}')
async def get_account(id):
    return service.getAccount(id)

@app.get('/api/account/open/{custid}')
async def open_account(custid):
    return service.createAccount(25,custid)

@app.get('/api/account/close/{acctid}')
async def open_account(acctid):
    return service.closeAccount(acctid)

@app.get('/api/account/withdrawal/{custid}/{amount}')
async def open_account(custid,amount):
    return service.withdrawal(float(amount),custid)

@app.get('/api/account/deposit/{custid}/{amount}')
async def open_account(custid,amount):
    return service.deposit(float(amount),custid)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True,
                timeout_keep_alive=3600, debug=True, workers=10)
