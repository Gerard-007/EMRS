import sqlite3
from api.user import User


class Patient(User):
    def __init__(self, first_name, last_name, dob, address, phone_number, email, med_history=None, assigned_doctor=None):
        super().__init__(first_name, last_name, dob, address, phone_number, email)
        self.med_history = med_history or {}
        self.assigned_doctor = assigned_doctor

    def save_to_db(self, db):
        super().save_to_db(db)  # Save base User data
        conn = db.create_connection()
        if conn:
            try:
                # Get the user ID (assuming last user is the current one)
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
                user_id = cursor.fetchone()[0]

                # Insert into patients
                cursor.execute('''
                    INSERT INTO patients (id, medical_history)
                    VALUES (?, ?)
                ''', (user_id, str(self.med_history)))

                conn.commit()
                print(f"Patient {self.first_name} {self.last_name} saved to database.")
            except sqlite3.Error as e:
                print(f"Error saving patient to database: {e}")
            finally:
                conn.close()

    @classmethod
    def load_from_db(cls, db, patient_id):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()

                cursor.execute('''
                    SELECT u.first_name, u.last_name, u.dob, c.address, c.phone, c.email, p.medical_history
                    FROM users u
                    INNER JOIN contactInfos c ON u.contact_info_id = c.id
                    INNER JOIN patients p ON u.id = p.id
                    WHERE u.id = ?
                ''', (patient_id,))
                row = cursor.fetchone()

                if row:
                    return cls(
                        first_name=row[0],
                        last_name=row[1],
                        dob=row[2],
                        address=row[3],
                        phone_number=row[4],
                        email=row[5],
                        med_history=eval(row[6])
                    )
                else:
                    print(f"No patient found with ID {patient_id}.")
            except sqlite3.Error as e:
                print(f"Error loading patient from database: {e}")
            finally:
                conn.close()
