from api.user import User


class Doctor(User):
    def __init__(self, first_name, last_name, dob, address, phone, email, specialization):
        super().__init__(first_name, last_name, dob, address, phone, email)
        self.specialization = specialization

    def save_to_db(self, db):
        user_id = super().save_to_db(db, "doctor")
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO doctors (id, specialization)
                    VALUES (?, ?)
                ''', (user_id, self.specialization))
                conn.commit()
            finally:
                conn.close()