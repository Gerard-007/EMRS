from apps.patient import Patient
from apps.user import User


class Doctor(User):
    def __init__(self, first_name, last_name, dob, address, phone_number, email, specialization, assigned_patients, appointments):
        super().__init__(first_name, last_name, dob, address, phone_number, email)
        self.__specialization = specialization
        self.__assigned_patients = assigned_patients
        self.__appointments = appointments

    def update_medical_record(self, patient, new_diagnosis, test, drug):
        medical_history = patient.get_med_history()
        medical_history["diagnosis"] = new_diagnosis
        medical_history["test"] = test
        medical_history["drug"] = drug
        print(
            f"Patient {patient.first_name + " " + patient.last_name}'s medical history has been updated by Dr. {self.first_name + " " + self.last_name}")
        return medical_history

    def update_appointment(self, patient, date, time):
        for appointment in self.__appointments:
            if appointment.date == date and appointment.time == time:
                print(f"Conflict detected: Doctor {self.doctor} already has an appointment at this time.")
                return

            if appointment.patient == patient.first_name:
                appointment.date = date
                appointment.time = time
        print(
            f"Patient {patient.first_name + " " + patient.last_name}'s appointment has been updated by Dr. {self.first_name + " " + self.last_name}")

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

    def get_appointments(self):
        return self.__appointments

