from datetime import datetime
from appointment import Appointment

from user import User

class Frontdesk(User):
    def __init__(self, first_name, last_name, dob, address, phone, email):
        super().__init__(first_name, last_name, dob, address, phone, email)
        self.patients = []
        self.appointments = []

    def book_appointment(self, date, time, doctor, patient):
        Appointment.book_an_appointment(date, time, doctor, patient)

    def register_patient(self, user):
        ...

    def search(self, value):
        ...

    def generate_medical_records(self, patient):
        ...

    def __str__(self):
        return f"Frontdesk(appointment={self.appointment})"


