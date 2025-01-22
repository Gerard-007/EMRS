from api.user import User


class Patient(User):
    def __init__(self, first_name, last_name, dob, address, phone, email, medical_history):
        super().__init__(first_name, last_name, dob, address, phone, email)
        self.medical_history = medical_history

    def save_to_db(self, db):
        user_id = super().save_to_db(db, "patient")
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO patients (id, medical_history)
                    VALUES (?, ?)
                ''', (user_id, self.medical_history))
                conn.commit()
            finally:
                conn.close()
