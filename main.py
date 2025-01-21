
from apps.contact import ContactInfo
from apps.user import User


if __name__ == "__main__":
    contact = ContactInfo("123 Main St", "555-1234", "user@example.com")
    user = User("John", "Doe", "1990-01-01", contact)

    print(user)
    # John Doe, DOB: 1990-01-01, Contact: Address: 123 Main St, Phone: 555-1234, Email: user@example.com