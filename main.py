from model.Account import Account
from repository.AccountRepository import AccountRepository

account = Account(None, 'other', 1, 0.0)

repo = AccountRepository()
# repo.insert(account)
data = repo.get(24)
print(data)