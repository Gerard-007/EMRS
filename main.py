
from apps.contact import ContactInfo
from apps.frontdesk import FrontDesk
from apps.user import User

def display_mainmenu():
    print("---WELCOME TO GOD-CARE'S HOSPITAL")
    print("Select an option")
    print("1- FrontDesk")
    print("2- Patient")
    print("3- Doctor")
    print("4- Exit")

def display_Frontdesk_menu():
    print("---WELCOME TO GOD-CARE'S HOSPITAL")
    print("Select an option")
    print("1- Register patient")
    print("2- Book Appointment")
    print("3- Search")
    print("4- Generate medical-report")
    print("5- Exit")

def display_Patient_menu():
    print("---WELCOME TO GOD-CARE'S HOSPITAL")
    print("Select an option")
    print("1- Check medical history")
    print("2- Check Assigned Doctor")
    print("3- Check Appointment")
    print("4- Exit")

def display_Doctor_menu():
    print("---WELCOME TO GOD-CARE'S HOSPITAL")
    print("Select an option")
    print("1- Check Assigned Patient")
    print("2- Update Appointment")
    print("3- Search")
    print("4- Update Medical Report")
    print("5- Exit")

if __name__ == "__main__":
    contact = ContactInfo("123 Main St", "555-1234", "user@example.com")
    user = User("John", "Doe", "1990-01-01", contact)

    print(user)
    # John Doe, DOB: 1990-01-01, Contact: Address: 123 Main St, Phone: 555-1234, Email: user@example.com