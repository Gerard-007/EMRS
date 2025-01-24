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
        first_name = patient.first_name[0] if isinstance(patient.first_name, list) and patient.first_name else patient.first_name
        last_name = patient.last_name[0] if isinstance(patient.last_name, list) and patient.last_name else patient.last_name
        if name.lower() in (first_name + " " + last_name).lower():
            return patient
    return None

def find_doctor_by_name(name):
    for doctor in doctors:
        first_name = doctor.first_name[0] if isinstance(doctor.first_name, list) and doctor.first_name else doctor.first_name
        last_name = doctor.last_name[0] if isinstance(doctor.last_name, list) and doctor.last_name else doctor.last_name
        if name.lower() in (first_name + " " + last_name).lower():
            return doctor
    return None

def get_patient():
    patient_name = input("Enter the patient's name: ").strip()
    patient = find_patient_by_name(patient_name)
    if not patient:
        print("Patient not found. Please try again.")
        return
    return patient

def get_doctor():
    doctor_name = input("Enter the doctor's name: ").strip()
    doctor = find_doctor_by_name(doctor_name)
    if not doctor:
        print("Doctor not found. Please try again.")
        return
    return doctor
