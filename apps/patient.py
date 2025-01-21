from apps.user import User


class Patient(User):
    def __init__(self, first_name, last_name, dob, address, phone_number, email, med_history, appointments, patient_id,assigned_doctor):
        super().__init__(first_name, last_name, dob, address, phone_number, email)
        self.__med_history = med_history
        self.__appointments = appointments
        self.__patient_id = patient_id
        self.__assigned_doctor = assigned_doctor

    def check_appointments(self):
        print("Name \tDate\tTime")
        for appointment in self.__appointments:
            print(appointment.name, appointment.date, appointment.time)

    def view_med_history(self):
        for key in self.__med_history:
            print(f" {key} : {self.__med_history[key]}")

    def get_med_history(self):
        return self.__med_history

    def get_appointments(self):
        return self.__appointments





