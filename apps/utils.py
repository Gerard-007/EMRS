import random

patients = []
doctors = []
appointments = []


def generate_id(appointment, value):
    appointment.appointment_id = value
    if appointment.appointment_id in [a.appointment_id for a in appointment.doctor.appointments]:
        appointment.appointment_id = random.randint(000000, 999999)
        generate_id(appointment, appointment.appointment_id)
    return appointment.appointment_id


def find_patient_by_name(name):
    for patient in patients:
        if name.lower() in (patient.first_name + " " + patient.last_name).lower():
            return patient
    return None


def find_doctor_by_name(name):
    for doctor in doctors:
        if name.lower() in (doctor.first_name + " " + doctor.last_name).lower():
            return doctor
    return None

def get_patient():
    patient_name = input("Enter the patient's name: ")
    patient = find_patient_by_name(patient_name)

    if not patient:
        print("Patient not found. Please try again.")
        return
    return patient

def get_doctor():
    doctor_name = input("Enter the doctor's name: ")
    doctor = find_doctor_by_name(doctor_name)

    if not doctor:
        print("Doctor not found. Please try again.")
        return
    return doctor
