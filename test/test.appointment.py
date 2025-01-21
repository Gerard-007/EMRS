import unittest

from apps.appointment import Appointment


class TestAppointment(unittest.TestCase):

    def setUp(self):
        self.doctor = Doctor()
        self.patient = Patient()
        self.appointment = Appointment("2025-02-01", "10:00 AM", self.doctor, self.patient)
        self.doctor.appointments.append(self.appointment)
        self.patient.appointments.append(self.appointment)

    def test_create_appointment(self):
        self.assertEqual(self.appointment.date, "2025-02-01")
        self.assertEqual(self.appointment.time, "10:00 AM")
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.patient, self.patient)

    def test_update_appointment(self):
        self.appointment.update_an_appointment("2025-02-02", "11:00 AM")
        self.assertEqual(self.appointment.date, "2025-02-02")
        self.assertEqual(self.appointment.time, "11:00 AM")

    def test_update_conflict(self):
        conflicting_appointment = Appointment("2025-02-02", "11:00 AM", self.doctor, Patient("Jane Doe"))
        self.doctor.appointments.append(conflicting_appointment)
        with self.assertLogs(level='INFO') as log:
            self.appointment.update_an_appointment("2025-02-02", "11:00 AM")
        self.assertIn("Conflict detected", "".join(log.output))

    def test_cancel_appointment(self):
        self.appointment.cancel_an_appointment()
        self.assertNotIn(self.appointment, self.doctor.appointments)
        self.assertNotIn(self.appointment, self.patient.appointments)