class User:
    def __init__(self, first_name, last_name, dob, address, phone, email):
        super().__init__(address, phone, email)
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def __str__(self):
        contact_details = str(super().__str__()) if super().__str__() else "No contact info"
        return f"{self.first_name} {self.last_name}, DOB: {self.dob}, Contact: {contact_details}"
