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

def welcome_message():
    """
    Welcome message to user to show them the options menu
    """
    print("Welcome to your contact book. What would you like to do?")
    print("1. View contact")
    print("2. Change contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")

def select_choice():
    """
    Takes user input on what choice and runs relevent function
    """
    repeat = True
    while repeat == True:
            try:
                choice = int(input("Choose[1-5]: \n"))
            except ValueError:
                print("Please input number.")
                choice = 0
            if choice == 1:
                show_contacts()
            elif choice == 2:
                print("\n==============")
                print("Change Contact")
                print("==============")
                change_contact()
            elif choice == 3:
                print("\n===========")
                print("Add Contact")
                print("===========")
                add_contact()
            elif choice == 4:
                delete_contact()
                print("4 selected")
            elif choice == 5:
                print("Thank you for using contact book. Good bye!")
                break
            else: 
                print("Choice unavailable.")

def push_to_sheets():
    """
    Pushes updated contacts list to Google sheets
    """

def show_contacts():
    """
    Print Google Sheets Values to console to show all contacts
    """
    df = pd.DataFrame(data)
    print(df.head(10))

def change_contact():
    """
    Changes existing contact on contacts list
    """

def add_contact():
    """
    Adds new contact to dictionary
    """
    name = input("Please Enter A Name: \n")
    phone_number = input("Please Enter A Phone Number: \n")
    email = input("Please Enter An Email Address: \n")
    address = input("Please Enter An Address: \n")

    contact_info.extend((name, phone_number, email, address))

    return contact_info

    print(f"{name}'s Phone Number Added Successfully")
    

def delete_contact():
    """
    Deletes contact from dictionary
    """

welcome_message()
select_choice()
update_worksheet(contact_info, 'contact')