from datetime import datetime

class Customer:
    def __init__(self, first_name: str, last_name: str, email: str, 
                 phone: str, address: str, city: str, state: str, zipcode: str, created_at=datetime.now()):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.created_at = created_at
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    
    def to_dict(self):
        diction = {"First Name": self.first_name,
                   "Last Name": self.last_name,
                   "Email": self.email,
                   "Phone Number": self.phone,
                   "Address": self.address,
                   "City": self.city,
                   "State": self.state,
                   "Zipcode": self.zipcode,
                   "Created At": self.created_at}
        return diction