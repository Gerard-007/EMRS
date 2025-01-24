from apps.user import User
import datetime


class Patient(User):
    def __init__(self, first_name, last_name, dob, address, phone, email, med_history=None, assigned_doctor=None):
        super().__init__(first_name, last_name, dob, address, phone, email)
        self.__med_history = med_history or {}
        self.__appointments = []
        self.__patient_id = datetime.datetime.now().strftime("%H%M%S")
        self.__assigned_doctor = assigned_doctor

    def __str__(self):
        doctor = f"Assigned Doctor: {self.__assigned_doctor.first_name} {self.__assigned_doctor.last_name}" if self.__assigned_doctor else "No assigned doctor"
        return f"{super().__str__()}, Patient ID: {self.__patient_id}, {doctor}"

    def check_appointments(self):
        print("Name \tDate\tTime")
        for appointment in self.__appointments:
            print(appointment.name, appointment.date, appointment.time)

    def view_med_history(self):
        for key in self.__med_history:
            print(f" {key} : {self.__med_history[key]}")
    def get_assigned_doctor(self):
        return self.__assigned_doctor

    def get_med_history(self):
        return self.__med_history or "Medical History not found"

    def get_appointments(self):
        return self.__appointments
