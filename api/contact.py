class ContactInfo:
    def __init__(self, address, phone, email):
        self.address = address
        self.phone = phone
        self.email = email

    def save_to_db(self, db):
        conn = db.create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO contactInfos (address, phone, email)
                    VALUES (?, ?, ?)
                ''', (self.address, self.phone, self.email))
                conn.commit()
                return cursor.lastrowid
            finally:
                conn.close()

    def __str__(self):
        return f"Address: {self.address}, Phone: {self.phone}, Email: {self.email}"
