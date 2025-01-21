import datetime

class Appointment:
    def __init__(self, date, time, doctor, patient):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
        self.appointment_id = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def update_an_appointment(self, date, time):
        for appointment in self.doctor.appointments:
            if appointment.date == date and appointment.time == time:
                print(f"Conflict detected: Doctor {self.doctor} already has an appointment at this time.")
                return
        self.date = date
        self.time = time
        print(f'Appointment {self.appointment_id} updated: {self}')

    def cancel_an_appointment(self):
        if self in self.doctor.appointments:
            self.doctor.appointments.remove(self)
            print(f"Removed from Doctor {self.doctor}'s schedule.")
        else:
            print(f"Appointment not found in Doctor {self.doctor}'s schedule.")
        if self in self.patient.appointments:
            self.patient.appointments.remove(self)
            print(f"Removed from Patient {self.patient}'s schedule.")
        else:
            print(f"Appointment not found in Patient {self.patient}'s schedule.")
        print(f'Appointment {self.appointment_id} canceled.')

    def __str__(self):
        return f'Appointment {self.appointment_id} for {self.patient} with Doctor {self.doctor} on {self.date} at {self.time}'
