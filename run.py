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

df = pd.DataFrame(data)
print(df.head(10))

contacts = {
    1 : {
        "name" : "Michael Dowling",
        "number" : "0851330885",
        "email" : "md@gmail.com",
        "address" : "14 Long Mile Rd"
    },
    2 : {
        "name" : "Jenny Connolly",
        "number" : "0863830895",
        "email" : "jc@gmail.com",
        "address" : "16 Hill Drive Rd"
    },
    3 : {
        "name" : "John Smith",
        "number" : "0869830885",
        "email" : "js@gmail.com",
        "address" : "147 Johnston Avenue"
    }
}

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

    select_choice()


def select_choice():
    while True:
            try:
                choice = int(input("Choose[1-5]: \n"))
            except ValueError:
                print("Please input number.")
                choice = 0
            if choice == 1:
                show_contacts()
                welcome_message()
            elif choice == 2:
                print("\n==============")
                print("Change Contact")
                print("==============")
                change_contact()
                welcome_message()
            elif choice == 3:
                print("\n===========")
                print("Add Contact")
                print("===========")
                add_contact()
                welcome_message()
            elif choice == 4:
                delete_contact()
                welcome_message()
                print("4 selected")
            elif choice == 5:
                print("Thank you for using contact book. Good bye!")
                break
            else: 
                print("Choice unavailable.")




def add_contact(name, phone_no, email_address, company, worksheet):
    print(f"Updating Contact Book...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(name, phone_no, email_address, company,)
    print(f'{worksheet} worksheet updated successfully\n')

add_contact(name, phone_no, email_address, company, worksheet)