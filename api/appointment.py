import sqlite3
from api.database.db_config import Database


class Appointment:
    def __init__(self, date, time, doctor_id, patient_id, details=None, appointment_id=None):
        self.date = date
        self.time = time
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.details = details
        self.appointment_id = appointment_id or f"{date.replace('-', '')}{time.replace(':', '')}{doctor_id}{patient_id}"

    def save_to_db(self, db):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO appointments (appointment_id, date, time, details, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    self.appointment_id,
                    self.date,
                    self.time,
                    self.details,
                    self.doctor_id,
                    self.patient_id,
                ))

                conn.commit()
                print(f"Appointment {self.appointment_id} saved to database.")
            except sqlite3.Error as e:
                print(f"Error saving appointment to database: {e}")
            finally:
                conn.close()

    @classmethod
    def load_from_db(cls, db, appointment_id):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT date, time, details, doctor_id, patient_id
                    FROM appointments
                    WHERE appointment_id = ?
                ''', (appointment_id,))
                row = cursor.fetchone()

                if row:
                    return cls(
                        date=row[0],
                        time=row[1],
                        details=row[2],
                        doctor_id=row[3],
                        patient_id=row[4],
                        appointment_id=appointment_id,
                    )
                else:
                    print(f"No appointment found with ID {appointment_id}.")
            except sqlite3.Error as e:
                print(f"Error loading appointment from database: {e}")
            finally:
                conn.close()