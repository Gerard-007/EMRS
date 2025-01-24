from apps.contact import ContactInfo


class User:
    def __init__(self, first_name, last_name, dob, address, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.contact_info = ContactInfo(address, phone, email)

    def __str__(self):
        contact_details = str(self.contact_info)
        return f"{self.first_name} {self.last_name}, DOB: {self.dob}, Contact: {contact_details}"
