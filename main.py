import datetime
from apps.frontdesk import FrontDesk
from apps.medical_records import MedicalRecord
from apps.appointment import Appointment
from apps.doctor import Doctor
from apps.patient import Patient
from apps.utils import *


def display_welcome():
    print("---WELCOME TO GOD-CARE'S HOSPITAL")
    print("Select an option")

def display_mainmenu():
    display_welcome()
    return input("""
    1- FrontDesk
    2- Patient
    3- Doctor
    0- Exit
    >> """)

def display_frontdesk_menu():
    display_welcome()
    return input("""
    1- Register patient
    2- Register doctor
    3- Book Appointment
    4- Search
    5- Generate medical-report
    0 Exit
    >> """)

def display_patient_menu():
    display_welcome()
    return input("""
    1- Check medical history
    2- Check Assigned Doctor
    0- Exit
    >> """)

def display_doctor_menu():
    display_welcome()
    return input(
    """
    1- Check Assigned Patient
    2- Update Appointment
    3- Search
    4- Update Medical Report
    0- Exit
    >> """)


def register_patient():
    first_name = input("Enter first name: ").split()
    last_name = input("Enter last name: ").split()
    dob = input("Enter date of birth(YYYY-MM-DD): ").split()
    address = input("Enter address: ").split()
    phone_number = input("Enter phone number: ").split()
    email = input("Enter email: ").split()
    patient = Patient(
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        address=address,
        phone=phone_number,
        email=email
    )
    patients.append(patient)

def register_doctor():
    first_name = input("Enter first name: ").split()
    last_name = input("Enter last name: ").split()
    dob = input("Enter date of birth(YYYY-MM-DD): ").split()
    address = input("Enter address: ").split()
    phone_number = input("Enter phone number: ").split()
    email = input("Enter email: ").split()
    specialization = input("Enter specialization: ").split()
    doctor = Doctor(
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        address=address,
        phone=phone_number,
        email=email,
        specialization=specialization
    )
    doctors.append(doctor)


def book_appointment():
    print("Booking an appointment...")
    date = input("Enter the appointment date (YYYY-MM-DD): ").split()
    time = input("Enter the appointment time (HH:MM): ").split()
    patient = get_patient()
    doctor = get_doctor()
    appointment = Appointment(date, time, doctor, patient)
    try:
        doctor.get_appointments().append(appointment)
        patient.get_appointments().append(appointment)
        print(f"Appointment booked successfully: {appointment}")
    except AttributeError as e:
        print("Doctor or patient not found")

def search_patient():
    search_query = input("Enter the patient's name to search: ")
    results = [p for p in patients if search_query.lower() in p.first_name[0].lower() or search_query.lower() in p.last_name[0].lower()]
    if results:
        for patient in results:
            print(f"Found patient: {patient.first_name[0]} {patient.last_name[0]}")  # Print patient details
    else:
        print("No patients found.")

def generate_medical_report():
    print("Generating a medical report...")
    patient = get_patient()
    print(f"Medical Report for {patient.first_name[0]} {patient.last_name[0]}:")
    patient.view_med_history()


def check_medical_history():
    print("Checking medical history...")
    patient = get_patient()
    if patient.get_med_history():
        print("Medical History:")
        patient.view_med_history()
    else:
        print("No medical history available.")

def check_assigned_doctor():
    patient = get_patient()
    assigned_doctor = patient.get_assigned_doctor()
    if assigned_doctor:
        print(f"Assigned Doctor: Dr. {assigned_doctor.first_name} {assigned_doctor.last_name}")
    else:
        print("No doctor assigned.")


def check_assigned_patients():
    print("Checking assigned patients...")
    doctor = get_doctor()
    patients = doctor.get_assigned_patients()
    if patients:
        print("Assigned Patients:")
        for patient in patients:
            print(f"{patient.first_name} {patient.last_name}")
    else:
        print("No patients assigned.")

def update_doctor_appointment():
    print("Updating an appointment...")
    date = input("Enter the new appointment date (YYYY-MM-DD): ")
    time = input("Enter the new appointment time (HH:MM): ")
    doctor = get_doctor()
    patient = get_patient()

    if doctor.update_appointment(patient, date, time):
        print("Appointment updated successfully.")
    else:
        print("Failed to update appointment try again.")

def search_for_patient_or_appointment():
    search_value = input("Enter the name or appointment detail to search: ")
    get_doctor().search(search_value)

def update_medical_report():
    print("Updating medical report...")
    doctor = get_doctor()
    patient = get_patient()

    diagnosis = input("Enter the new diagnosis: ")
    medications = input("Enter the medications (comma-separated): ").split(",")
    notes = input("Enter additional notes: ")

    record = MedicalRecord(patient, doctor, diagnosis, medications, notes, datetime.date.today())
    print("Medical report updated successfully:")
    print(record)


def main():
    while True:
        option = display_mainmenu()
        match option:
            case "1":
                while True:
                    frontdesk_option = display_frontdesk_menu()
                    match frontdesk_option:
                        case "1":
                            register_patient()
                        case "2":
                            register_doctor()
                        case "3":
                            book_appointment()
                        case "4":
                            search_patient()
                        case "5":
                            generate_medical_report()
                        case "0":
                            print("Exiting FrontDesk menu...")
                            break
                        case _:
                            print("Invalid choice. Please try again.")

            case "2":
                while True:
                    patient_option = display_patient_menu()
                    match patient_option:
                        case "1":
                            check_medical_history()
                        case "2":
                            check_assigned_doctor()
                        case "0":
                            print("Exiting Patient menu...")
                            break
                        case _:
                            print("Invalid choice. Please try again.")

            case "3":
                while True:
                    doctor_option = display_doctor_menu()
                    match doctor_option:
                        case "1":
                            print("Checking assigned patients...")
                            check_assigned_patients()
                        case "2":
                            print("Updating an appointment...")
                            update_doctor_appointment()
                        case "3":
                            print("Searching for a patient or appointment...")
                            search_for_patient_or_appointment()
                        case "4":
                            print("Updating a medical report...")
                            update_medical_report()
                        case "0":
                            print("Exiting Doctor menu...")
                            break
                        case _:
                            print("Invalid choice. Please try again.")

            case "0":
                print("Thank you for visiting God-Care's Hospital. Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
