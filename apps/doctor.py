from apps.user import User


class Doctor(User):
    def __init__(self, first_name, last_name, dob, address, phone_number, email, specialization):
        super().__init__(first_name, last_name, dob, address, phone_number, email)
        self.__specialization = specialization
        self.__assigned_patients = []
        self.__appointments = []

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
                print(f"Conflict detected: Doctor {self.first_name} {self.last_name} already has an appointment at this time.")
                return False

        for appointment in self.__appointments:
            if appointment.patient == patient:
                appointment.date = date
                appointment.time = time
                print(f"Updated appointment for {patient.first_name} {patient.last_name} to {date} at {time}.")
                return True

        print(f"No existing appointment found for {patient.first_name} {patient.last_name}.")
        return False

    def search(self, value):
        patient_results = [
            p for p in self.__assigned_patients
            if value.lower() in p.first_name.lower() or value.lower() in p.last_name.lower()
        ]
        if patient_results:
            print("Matching Patients:")
            for patient in patient_results:
                print(f"{patient.first_name} {patient.last_name}")

        appointment_results = [
            a for a in self.__appointments
            if value.lower() in a.patient.first_name.lower()
            or value.lower() in a.patient.last_name.lower()
            or value.lower() in a.date.lower()
            or value.lower() in a.time.lower()
        ]
        if appointment_results:
            print("Matching Appointments:")
            for appointment in appointment_results:
                print(appointment)
        else:
            print("No matches found.")

    def get_appointments(self):
        return self.__appointments

    def get_assigned_patients(self):
        return self.__assigned_patients
