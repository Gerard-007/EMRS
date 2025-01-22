from apps.contact import ContactInfo
from apps.frontdesk import FrontDesk
from apps.user import User
from database.db_config import Database

def display_mainmenu():
    return input("""
    ---WELCOME TO GOD-CARE'S HOSPITAL
    Select an option
    1- FrontDesk
    2- Patient
    3- Doctor
    4- Exit""")

def display_frontdesk_menu():
    return input("""
    ---WELCOME TO GOD-CARE'S HOSPITAL")
    Select an option
    1- Register patient
    2- Book Appointment
    3- Search
    4- Generate medical-report
    5- Exit""")

def display_patient_menu():
    return input("""---WELCOME TO GOD-CARE'S HOSPITAL
    Select an option
    1- Check medical history
    2- Check Assigned Doctor
    4- Exit""")

def display_doctor_menu():
    return input(
    """---WELCOME TO GOD-CARE'S HOSPITAL
    Select an option
    1- Check Assigned Patient
    2- Update Appointment
    3- Search
    4- Update Medical Report
    5- Exit""")

def main():
    # Initialize database
    db = Database()
    
    while True:
        option = display_mainmenu()
        match option:
            case "1":
                while True:
                    frontdesk_option = display_frontdesk_menu()
                    match frontdesk_option:
                        case "1":
                            print("Registering a patient...")
                        case "2":
                            print("Booking an appointment...")
                        case "3":
                            print("Searching for a patient...")
                        case "4":
                            print("Generating a medical report...")
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
                            print("Checking medical history...")
                        case "2":
                            print("Checking assigned doctor...")
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
                        case "2":
                            print("Updating an appointment...")
                        case "3":
                            print("Searching for a patient or appointment...")
                        case "4":
                            print("Updating a medical report...")
                        case "5":
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
