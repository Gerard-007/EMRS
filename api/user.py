from api.contact import ContactInfo

class User:
    def __init__(self, first_name, last_name, dob, address, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.contact_info = ContactInfo(address, phone, email)

    def save_to_db(self, db, user_type):
        contact_info_id = self.contact_info.save_to_db(db)
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (first_name, last_name, dob, user_type, contact_info_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.first_name, self.last_name, self.dob, user_type, contact_info_id))
                conn.commit()
                return cursor.lastrowid
            finally:
                conn.close()

    def __str__(self):
        contact_details = str(self.contact_info)
        return f"{self.first_name} {self.last_name}, DOB: {self.dob}, Contact: {contact_details}"
