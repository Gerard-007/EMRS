class User:
    def __init__(self, first_name, last_name, dob, contact_info=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.contact_info = contact_info

    def __str__(self):
        contact_details = str(self.contact_info) if self.contact_info else "No contact info"
        return f"{self.first_name} {self.last_name}, DOB: {self.dob}, Contact: {contact_details}"
