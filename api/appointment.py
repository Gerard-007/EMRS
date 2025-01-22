import datetime


class Appointment:
    def __init__(self, date, time, details, doctor, patient):
        self.date = date
        self.time = time
        self.details = details
        self.doctor = doctor
        self.patient = patient
        self.appointment_id = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def save_to_db(self, db):
        if conn := db.create_connection():
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO appointments (appointment_id, date, time, details, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (self.appointment_id, self.date, self.time, self.details,
                      self.doctor.id, self.patient.id))
                conn.commit()
            finally:
                conn.close()
