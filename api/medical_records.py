import datetime
from api.database.db_config import Database


class MedicalRecord:
    def __init__(self, patient, doctor, diagnosis, medications, notes, date=None):
        self.patient = patient  # Patient object
        self.doctor = doctor    # Doctor object
        self.diagnosis = diagnosis
        self.medications = medications
        self.notes = notes
        self.date = date or datetime.date.today()

    def save_to_db(self):
        conn = Database().create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO medicalRecords (date, diagnosis, medications, notes, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (self.date, self.diagnosis, 
                      ", ".join(self.medications) if self.medications else None,
                      self.notes, self.doctor.id, self.patient.id))
                conn.commit()
                print("Medical record saved successfully.")
            except Exception as e:
                print(f"Error saving medical record: {e}")
            finally:
                conn.close()

    def update_in_db(self):
        conn = Database().create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE medicalRecords
                    SET diagnosis = ?, medications = ?, notes = ?, date = ?
                    WHERE doctor_id = ? AND patient_id = ?
                ''', (self.diagnosis, 
                      ", ".join(self.medications) if self.medications else None,
                      self.notes, self.date, self.doctor.id, self.patient.id))
                conn.commit()
                print("Medical record updated successfully.")
            except Exception as e:
                print(f"Error updating medical record: {e}")
            finally:
                conn.close()

    @staticmethod
    def fetch_records(patient_id):
        conn = Database().create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM medicalRecords
                    WHERE patient_id = ?
                ''', (patient_id,))
                return cursor.fetchall()
            except Exception as e:
                print(f"Error fetching medical records: {e}")
            finally:
                conn.close()

    def __str__(self):
        medications_str = ", ".join(self.medications) if self.medications else "None"
        return (f"""
        Medical Record for {self.patient.first_name} {self.patient.last_name}
        Doctor: {self.doctor.first_name} {self.doctor.last_name}
        Date: {self.date}
        Diagnosis: {self.diagnosis}
        Medications: {medications_str}
        Notes: {self.notes}""")

