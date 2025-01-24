import sqlite3
from api.user import User


class Doctor(User):
    def __init__(self, first_name, last_name, dob, address, phone_number, email, specialization):
        super().__init__(first_name, last_name, dob, address, phone_number, email)
        self.specialization = specialization

    def save_to_db(self, db):
        super().save_to_db(db)
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
                user_id = cursor.fetchone()[0]

                cursor.execute('''
                    INSERT INTO doctors (id, specialization)
                    VALUES (?, ?)
                ''', (user_id, self.specialization))

                conn.commit()
                print(f"Doctor {self.first_name} {self.last_name} saved to database.")
            except sqlite3.Error as e:
                print(f"Error saving doctor to database: {e}")
            finally:
                conn.close()

    @classmethod
    def load_from_db(cls, db, doctor_id):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()

                cursor.execute('''
                    SELECT u.first_name, u.last_name, u.dob, c.address, c.phone, c.email, d.specialization
                    FROM users u
                    INNER JOIN contactInfos c ON u.contact_info_id = c.id
                    INNER JOIN doctors d ON u.id = d.id
                    WHERE u.id = ?
                ''', (doctor_id,))
                row = cursor.fetchone()

                if row:
                    return cls(
                        first_name=row[0],
                        last_name=row[1],
                        dob=row[2],
                        address=row[3],
                        phone_number=row[4],
                        email=row[5],
                        specialization=row[6]
                    )
                else:
                    print(f"No doctor found with ID {doctor_id}.")
            except sqlite3.Error as e:
                print(f"Error loading doctor from database: {e}")
            finally:
                conn.close()
