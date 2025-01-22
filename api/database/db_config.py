import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.db_file = "emrs.db"
        self.conn = None
        self.create_tables()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        conn = self.create_connection()
        if conn:
            try:
                cursor = conn.cursor()

                # Create ContactInfo table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS contactInfos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        address TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT NOT NULL
                    )
                ''')

                # Create Users table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        dob TEXT NOT NULL,
                        user_type TEXT NOT NULL,
                        contact_info_id INTEGER,
                        FOREIGN KEY (contact_info_id) REFERENCES contactInfos (id)
                    )
                ''')

                # Create Doctors table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS doctors (
                        id INTEGER PRIMARY KEY,
                        specialization TEXT NOT NULL,
                        FOREIGN KEY (id) REFERENCES users (id)
                    )
                ''')

                # Create Patients table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        medical_history TEXT,
                        FOREIGN KEY (id) REFERENCES users (id)
                    )
                ''')

                # Create Appointments table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        appointment_id TEXT UNIQUE NOT NULL,
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        details TEXT,
                        doctor_id INTEGER NOT NULL,
                        patient_id INTEGER NOT NULL,
                        FOREIGN KEY (doctor_id) REFERENCES doctors (id),
                        FOREIGN KEY (patient_id) REFERENCES patients (id)
                    )
                ''')

                # Create MedicalRecords table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS medicalRecords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        diagnosis TEXT,
                        medications TEXT,
                        notes TEXT,
                        doctor_id INTEGER NOT NULL,
                        patient_id INTEGER NOT NULL,
                        FOREIGN KEY (doctor_id) REFERENCES doctors (id),
                        FOREIGN KEY (patient_id) REFERENCES patients (id)
                    )
                ''')

                conn.commit()
            except Error as e:
                print(f"Error creating tables: {e}")
            finally:
                conn.close()
