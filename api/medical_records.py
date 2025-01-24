import sqlite3
from api.database.db_config import Database


class MedicalRecord:
    def __init__(self, patient_id, doctor_id, diagnosis, medications, notes, date):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.medications = medications or []
        self.notes = notes
        self.date = date

    def save_to_db(self, db):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO medicalRecords (date, diagnosis, medications, notes, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    self.date,
                    self.diagnosis,
                    ", ".join(self.medications),
                    self.notes,
                    self.doctor_id,
                    self.patient_id,
                ))

                conn.commit()
                print(f"Medical record for patient {self.patient_id} saved to database.")
            except sqlite3.Error as e:
                print(f"Error saving medical record to database: {e}")
            finally:
                conn.close()

    @classmethod
    def load_from_db(cls, db, record_id):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT date, diagnosis, medications, notes, doctor_id, patient_id
                    FROM medicalRecords
                    WHERE id = ?
                ''', (record_id,))
                row = cursor.fetchone()

                if row:
                    return cls(
                        date=row[0],
                        diagnosis=row[1],
                        medications=row[2].split(", "),
                        notes=row[3],
                        doctor_id=row[4],
                        patient_id=row[5],
                    )
                else:
                    print(f"No medical record found with ID {record_id}.")
            except sqlite3.Error as e:
                print(f"Error loading medical record from database: {e}")
            finally:
                conn.close()
