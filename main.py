from model.Account import Account
from repository.AccountRepository import AccountRepository

account = Account(21, '045oxs', 1, 5.0)

repo = AccountRepository()

repo.delete(account)