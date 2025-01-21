import unittest
from apps.doctor import Doctor
from apps.patient import Patient
from apps.appointment import Appointment


class TestDoctor(unittest.TestCase):

    def test_doctor_can_update_patient_medical_record_successfully(self):
        medical_history = {"Name": "patient1", "diagnosis": "malaria", "test": "malaria_test", "drug": "lumaterm"}
        appointment = Appointment("1990-01-01", "10pm", "doctor", "patient")
        appointment2 = Appointment("1990-01-01", "11pm", "doctor2", "Name")
        appointments = [appointment, appointment2]
        patient1 = Patient("Name", "lastName", "1990-01-01", "address", "09098128958", "email", medical_history,
                           appointment, "001", "doctor")

        patient2 = Patient("Name", "lastName", "1990-01-01", "address", "09098128958", "email", medical_history,
                           appointment, "002", "doctor")

        assigned_patients = [patient1, patient2]

        doctor = Doctor("Name", "lastName", "1990-01-01", "address", "09098128958", "email", "dentist",
                        assigned_patients,appointments)
        new_medical_history = doctor.update_medical_record(assigned_patients[0], "fever", "fever_test", "fever_drug")
        expected_medical_history = {"Name": "patient1", "diagnosis": "fever", "test": "fever_test",
                                    "drug": "fever_drug"}

        self.assertEqual(new_medical_history, expected_medical_history)

    def test_doctor_can_update_patient_appointment_successfully(self):
        medical_history = {"Name": "patient1", "diagnosis": "malaria", "test": "malaria_test", "drug": "lumaterm"}
        appointment = Appointment("1990-01-01", "10pm", "doctor", "patient")
        appointment2 = Appointment("1990-01-01", "11pm", "doctor2", "Name")
        appointments = [appointment, appointment2]
        patient1 = Patient("Name", "lastName", "1990-01-02", "address", "09098128958", "email", medical_history,
                           appointments, "001", "doctor")
        patient2 = Patient("Name", "lastName", "1990-01-01", "address", "09098128958", "email", medical_history,
                           appointments, "002", "doctor")
        assigned_patients = [patient1, patient2]
        doctor = Doctor("Name", "lastName", "1990-01-01", "address", "09098128958", "email", "dentist",
                        assigned_patients, appointments)
        doctor.update_appointment(assigned_patients[0], "1990-01-02", "10pm")

        self.assertEqual(doctor.get_appointments()[1].date, "1990-01-02")


