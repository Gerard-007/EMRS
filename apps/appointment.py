import random


class Appointment:
    def __init__(self, date, time, doctor, patient):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
        self.appointment_id = random.randint(100000, 999999)

    def book_an_appointment(self, date, time, doctor, patient):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
        doctor.appointments.append(self)
        patient.appointments.append(self)
        print(f'Appointment {self.appointment_id} booked for {patient} with Doctor {doctor} on {date} at {time}')

    def update_an_appointment(self, date, time):
        self.date = date
        self.time = time
        print(f'Appointment {self.appointment_id} updated: {self}')

    def cancel_an_appointment(self):
        if self in self.doctor.appointments:
            self.doctor.appointments.remove(self)
        if self in self.patient.appointments:
            self.patient.appointments.remove(self)
        print(f'Appointment {self.appointment_id} canceled.')

    def __str__(self):
        return f'Appointment {self.appointment_id} for {self.patient} with Doctor {self.doctor} on {self.date} at {self.time}'
