from api.database.db_config import Database
from api.medical_records import MedicalRecord
from api.user import User
import datetime


class FrontDesk(User):
    def __init__(self, first_name, last_name, dob, address, phone, email):
        super().__init__(first_name, last_name, dob, address, phone, email)

    def register_patient(self, patient):
        conn = Database().create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO patients (id, medical_history)
                    VALUES (?, ?)
                ''', (patient.id, None))  # Initially, no medical history
                conn.commit()
                print(f"Patient {patient.first_name} {patient.last_name} registered successfully.")
            except Exception as e:
                print(f"Error registering patient: {e}")
            finally:
                conn.close()

    def book_appointment(self, date, time, doctor, patient, details=""):
        conn = Database().create_connection()
        if conn:
            try:
                # Ensure no conflicts with existing appointments
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM appointments
                    WHERE doctor_id = ? AND date = ? AND time = ?
                ''', (doctor.id, date, time))
                if cursor.fetchone():
                    print(f"Conflict: Doctor {doctor.first_name} {doctor.last_name} already has an appointment.")
                    return

                # Book the appointment
                cursor.execute('''
                    INSERT INTO appointments (appointment_id, date, time, details, doctor_id, patient_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", date, time, details, doctor.id, patient.id))
                conn.commit()
                print(f"Appointment booked for {patient.first_name} with Doctor {doctor.first_name} on {date} at {time}.")
            except Exception as e:
                print(f"Error booking appointment: {e}")
            finally:
                conn.close()

    def search_patient(self, value):
        conn = Database().create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT first_name, last_name FROM users
                    WHERE (LOWER(first_name) LIKE ? OR LOWER(last_name) LIKE ?)
                    AND id IN (SELECT id FROM patients)
                ''', (f"%{value.lower()}%", f"%{value.lower()}%"))
                results = cursor.fetchall()
                if results:
                    for result in results:
                        print(f"Found: {result[0]} {result[1]}")
                else:
                    print("No matches found.")
            except Exception as e:
                print(f"Error searching for patient: {e}")
            finally:
                conn.close()

    def generate_medical_records(self, patient):
        records = MedicalRecord.fetch_records(patient.id)
        if records:
            for record in records:
                print(f"Date: {record[1]}, Diagnosis: {record[2]}, Medications: {record[3]}, Notes: {record[4]}")
        else:
            print(f"No medical records found for {patient.first_name} {patient.last_name}.")
