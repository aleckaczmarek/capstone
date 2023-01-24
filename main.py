from model.Account import Account
from repository.AccountRepository import AccountRepository

account = Account(None, '045oxs', 1, 0.0)

repo = AccountRepository()

repo.insert(account)