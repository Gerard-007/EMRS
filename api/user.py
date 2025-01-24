import sqlite3
from api.contact import ContactInfo


class User:
    def __init__(self, first_name, last_name, dob, address, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.contact_info = ContactInfo(address, phone, email)

    def save_to_db(self, db):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()

                cursor.execute('''
                    INSERT INTO contactInfos (address, phone, email)
                    VALUES (?, ?, ?)
                ''', (self.contact_info.address, self.contact_info.phone, self.contact_info.email))
                contact_info_id = cursor.lastrowid

                cursor.execute('''
                    INSERT INTO users (first_name, last_name, dob, user_type, contact_info_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.first_name, self.last_name, self.dob, type(self).__name__, contact_info_id))

                conn.commit()
                print(f"User {self.first_name} {self.last_name} saved to database.")
            except sqlite3.Error as e:
                print(f"Error saving user to database: {e}")
            finally:
                conn.close()
