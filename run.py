import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np

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

contact_info = []

def update_worksheet(data, worksheet):
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully\n')

def select_choice():
    """
    Welcome message to user to show them the options menu
    """
    print("Welcome to your contact book. What would you like to do?")
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




def show_contacts():
    """
    Print Google Sheets Values to console to show all contacts
    """
    df = pd.DataFrame(data)
    print(df.head(10))

def search_contact():
    """
    Searches contact in Google sheets and returns information
    """ 

def add_contact():
    """
    Takes inputted contact info and pushes to Google sheet.
    """
    while True:
        name = input("Please Enter A Name: \n")
        if valid_name(name):
            break
        else:
            print("Invalid name format. Please enter a name longer than 3 characters. Try again.")

    while True:
        phone = input("Please Enter A Phone Number: \n")
        if valid_phone(phone):
            break
        else:
            print("Invalid phone format. Please enter a 10 digit phone number. Try again.")

    while True:
        email = input("Please Enter An Email Address: \n")
        if valid_email(email):
            break
        else:
            print("Invalid email format. Please enter email containing an @ symbol. Try again.")
    
    while True:
        address = input("Please Enter An Address: \n")
        if valid_address(address):
            break
        else:
            print("Invalid address format. Please enter more than 3 characters. Try again.")

    row = [name, phone, email, address]
    contact_sheet.insert_row(row, 2)
    print(f"{name} added to contacts.")

def delete_contact():
    """
    Deletes contact from dictionary
    """

welcome_message()
select_choice()
update_worksheet(contact_info, 'contact')