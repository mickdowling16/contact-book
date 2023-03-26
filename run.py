import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')

contact_sheet = SHEET.worksheet('contact')
data = contact_sheet.get_all_values()


def valid_name(name):
    """Adds validation to the input for contact
    name to check for more than 3 characters"""
    if len(name) < 3:
        return False
    return True


def valid_phone(phone):
    """Adds validation to the input for contact phone
    number to check for 10 integars"""
    if len(phone) != 10:
        return False
    if not phone.isnumeric():
        return False
    return True


def valid_email(email):
    """Adds validation to the input for contact
    email address to check for @ or . """
    if '@' not in email or '.' not in email:
        return False
    return True


def select_choice():
    """
    Welcome message to user to show them the options menu
    """
    print("\nWelcome to your contact book. What would you like to do?")
    print("1. View contact")
    print("2. Search contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Enter choice: \n")

    try:
        choice = int(choice)
        if choice not in range(1, 6):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return select_choice()
    return choice


def get_contacts():
    """
    Returns all values from Google Sheet
    """
    return contact_sheet.get_all_records()


def show_contacts():
    """
    Print Google Sheets Values to console to show all contacts
    """
    contacts = get_contacts()
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("Contacts:")
        print(f"{'Name':<15} {'Phone':<25} {'Email':<20} {'Address':<25}")
        print("-" * 90)
        for contact in contacts:
            name = contact['Name']
            phone = contact['Phone']
            email = contact['Email']
            address = contact['Address']
            print(f"{name:<15} {phone:<25} {email:<20} {address:<25}")


def search_contact():
    """
    Searches contact in Google sheets and returns information
    """
    name = input("Enter the contact name: ").lower()
    try:
        cell = contact_sheet.find(name)
        row = cell.row
        contact = contact_sheet.row_values(row)
        print(f"Name: {contact[0]}")
        print(f"Phone: {contact[1]}")
        print(f"Email: {contact[2]}")
        print(f"Adress: {contact[3]}")

    except ValueError:
        print(f"{name} not found.")


def add_contact():
    """
    Takes inputted contact info and pushes to Google sheet.
    """
    while True:
        name = input("Please Enter A Name: \n").lower()
        if valid_name(name):
            break
        else:
            print("Please enter a name longer than 3")

    while True:
        phone = input("Please Enter A Phone Number: \n")
        if valid_phone(phone):
            break
        else:
            print("Please enter a10 digit phone number.")

    while True:
        email = input("Please Enter An Email Address: \n")
        if valid_email(email):
            break
        else:
            print("Please enter a valid email address")

    while True:
        address = input("Please Enter An Address: \n")
        break

    row = [name, phone, email, address]
    contact_sheet.insert_row(row, 2)
    print("+-+-+-+-+-+-+-+-+-+-+\n")
    print("...Loading...")
    print(f"{name} added to contacts\n.")


def delete_contact():
    """
    Deletes contact from dictionary
    """
    name = input("Enter the name of the contact to delete: ")

    cell = contact_sheet.find(name)
    if cell is None:
        print("Contact not found.")
        return

    row = cell.row

    contact_sheet.delete_rows(row)
    print("Contact deleted.")


while True:
    """
    Main programme loop. Takes user input and decides which function to run.
    """
    choice = select_choice()
    if choice == 1:
        show_contacts()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        add_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        print("Thank you for using Contact Book. Goodbye.")
        break
