from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    id: Optional[int] = None
    city: str
    state: str
    zipcode: str
    street: str

    def __init__(self,id, city, state, zipcode, street):
        super().__init__(id=id, city=city, state=state, zipcode=zipcode, street=street)


    def __eq__(self, other):
        return self.id == other.id and self.city == other.city and \
            self.state == other.state and self.zipcode == other.zipcode and \
                self.street == other.street