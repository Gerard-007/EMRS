import random
import re
from datetime import datetime

patients = []
doctors = []
appointments = []
medical_records = []

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

def validate_name(name):
    pattern = r'^[A-Za-z\s]+$'
    return bool(re.match(pattern, name))

def get_valid_name_input(prompt):
    while True:
        name = input(prompt).strip()
        if validate_name(name):
            return name
        print("Error: Please enter only alphabets and no special characters or numbers.")

def validate_address(address):
    pattern = r'^[A-Za-z0-9\s]+$'
    return bool(re.match(pattern, address))

def get_valid_address_input(prompt):
    while True:
        address = input(prompt).strip()
        if validate_address(address):
            return address
        print("Error: Please enter only letters and numbers eg . 123 Main St Anytown Nigeria")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt).strip()
        if validate_date(date_str):
            return date_str
        print("Error: Please enter date in YYYY-MM-DD format")

def validate_time(time_str):
    pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    return bool(re.match(pattern, time_str))

def get_valid_time_input(prompt):
    while True:
        time_str = input(prompt).strip()
        if validate_time(time_str):
            return time_str
        print("Error: Please enter time in HH:MM format (24-hour)")

def validate_phone(phone):
    pattern = r'^\d{11}$'
    return bool(re.match(pattern, phone))

def get_valid_phone_input(prompt):
    while True:
        phone = input(prompt).strip()
        if validate_phone(phone):
            return phone
        print("Error: Please enter exactly 11 digits (e.g., 08012345678)")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def get_valid_email_input(prompt):
    while True:
        email = input(prompt).strip()
        if validate_email(email):
            return email
        print("Error: Please enter a valid email address (e.g., example@email.com)")
