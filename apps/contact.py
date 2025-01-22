class ContactInfo:
    def __init__(self, address, phone, email):
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Address: {self.address}, Phone: {self.phone}, Email: {self.email}"
