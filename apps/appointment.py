import datetime
from database.db_config import Database

class Appointment:
    def __init__(self, date, time, details, doctor, patient):
        self.date = date
        self.time = time
        self.details = details
        self.doctor = doctor
        self.patient = patient
        self.appointment_id = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.db = Database()

    def save_to_db(self):
        conn = self.db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO appointments (appointment_id, date, time, details, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (self.appointment_id, self.date, self.time, self.details, 
                     self.doctor.id, self.patient.id))
                conn.commit()
                print(f"Appointment saved to database: {self.appointment_id}")
            except Exception as e:
                print(f"Error saving appointment: {e}")
            finally:
                conn.close()

    def update_an_appointment(self, date, time, details):
        conn = self.db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # Check for conflicts
                cursor.execute('''
                    SELECT * FROM appointments 
                    WHERE doctor_id = ? AND date = ? AND time = ? AND appointment_id != ?
                ''', (self.doctor.id, date, time, self.appointment_id))
                if cursor.fetchone():
                    print(f"Conflict detected: Doctor already has an appointment at this time.")
                    return

                cursor.execute('''
                    UPDATE appointments 
                    SET date = ?, time = ?, details = ?
                    WHERE appointment_id = ?
                ''', (date, time, details, self.appointment_id))

                conn.commit()
                self.date = date
                self.time = time
                self.details = details
                print(f'Appointment {self.appointment_id} updated')
            except Exception as e:
                print(f"Error updating appointment: {e}")
            finally:
                conn.close()

    def cancel_an_appointment(self):
        conn = self.db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM appointments 
                    WHERE appointment_id = ?
                ''', (self.appointment_id,))
                conn.commit()
                print(f'Appointment {self.appointment_id} canceled.')
            except Exception as e:
                print(f"Error canceling appointment: {e}")
            finally:
                conn.close()

    @staticmethod
    def get_appointments_by_doctor(doctor_id):
        db = Database()
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM appointments
                    WHERE doctor_id = ?
                ''', (doctor_id,))
                return cursor.fetchall()
            finally:
                conn.close()

    def __str__(self):
        return f'Appointment {self.appointment_id} for {self.patient} with Doctor {self.doctor} on {self.date} at {self.time}'
