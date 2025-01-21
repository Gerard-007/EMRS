from datetime import datetime
from appointment import Appointment
from user import User

class FrontDesk(User):
    def __init__(self, first_name, last_name, dob, address, phone, email):
        super().__init__(first_name, last_name, dob, address, phone, email)
        self.patients = []
        self.appointments = []

    def book_appointment(self, date, time, doctor, patient):
        appointment = Appointment.book_an_appointment(date, time, doctor, patient)
        self.appointments.append(appointment)
        doctor.appointments.append(appointment)
        patient.appointments.append(appointment)
        print(f"Appointment {appointment.appointment_id} booked for {patient.first_name} with Doctor {doctor.first_name} on {date} at {time}")

    def register_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            print(f"Patient {patient.first_name} {patient.last_name} registered successfully.")
        else:
            print(f"Patient {patient.first_name} {patient.last_name} is already registered.")

    def search(self, value):
        if results := [
            p
            for p in self.patients
            if value.lower() in p.first_name.lower()
            or value.lower() in p.last_name.lower()
        ]:
            for r in results:
                print(f"Found: {r.first_name} {r.last_name}")
        else:
            print("No matches found.")

    def generate_medical_records(self, patient):
        print(f"Medical Records for {patient.first_name} {patient.last_name}:")
        print("Medical History here...")
