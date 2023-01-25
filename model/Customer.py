from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    address_id: int
    email_address: str

    def __init__(self,id, first_name, last_name, address_id, email_address):
        super().__init__(id=id, first_name=first_name, last_name=last_name, address_id=address_id, email_address=email_address)


    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and \
            self.last_name == other.last_name and self.address_id == other.address_id and \
                self.email_address == other.email_address