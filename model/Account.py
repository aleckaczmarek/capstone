from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: Optional[int] = None
    account_number: str
    customer_id: int
    current_balance: float

    def updateBalance(self,amount):
        self.current_balance = amount

    def __init__(self,id, account_number,customer_id,current_balance):
        super().__init__(id=id, account_number=account_number, customer_id=customer_id, current_balance=current_balance)


    def __eq__(self, other):
        return self.id == other.id and self.account_number == other.account_number and \
            self.customer_id == other.customer_id and self.current_balance == other.current_balance