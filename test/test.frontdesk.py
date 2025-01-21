import unittest
from unittest.mock import MagicMock
from apps.frontdesk import FrontDesk  # Assuming FrontDesk is in frontdesk.py
from apps.user import User
from apps.appointment import Appointment

class TestFrontDesk(unittest.TestCase):

    def setUp(self):
        # Mock data
        self.front_desk = FrontDesk("Jane", "Doe", "1980-01-01", "123 Main St", "555-1234", "jane.doe@example.com")
        self.doctor = Doctor()
        self.patient = Patient()

        Appointment.book_an_appointment = MagicMock(return_value=Appointment("2025-02-01", "10:00 AM", self.doctor, self.patient))

    def test_register_patient(self):
        self.front_desk.register_patient(self.patient)
        self.assertIn(self.patient, self.front_desk.patients)
        self.front_desk.register_patient(self.patient)

    def test_book_appointment(self):
        self.front_desk.book_appointment("2025-02-01", "10:00 AM", self.doctor, self.patient)
        appointment = self.front_desk.appointments[0]
        self.assertIn(appointment, self.front_desk.appointments)
        self.assertIn(appointment, self.doctor.appointments)
        self.assertIn(appointment, self.patient.appointments)
        Appointment.book_an_appointment.assert_called_with("2025-02-01", "10:00 AM", self.doctor, self.patient)

    def test_search(self):
        patient_2 = Patient()
        self.front_desk.register_patient(self.patient)
        self.front_desk.register_patient(patient_2)

        with self.assertLogs(level='INFO') as log:
            self.front_desk.search("John")
        self.assertIn("Found: John Doe", "".join(log.output))

        with self.assertLogs(level='INFO') as log:
            self.front_desk.search("Smith")
        self.assertIn("Found: Jane Smith", "".join(log.output))

        with self.assertLogs(level='INFO') as log:
            self.front_desk.search("Nonexistent")
        self.assertIn("No matches found.", "".join(log.output))

    def test_generate_medical_records(self):
        with self.assertLogs(level='INFO') as log:
            self.front_desk.generate_medical_records(self.patient)
        self.assertIn("Medical Records for John Doe", "".join(log.output))
