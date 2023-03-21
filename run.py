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

contact = {
  "name": ["Michael Dowling", "Jenny Connolly", "Kieron Dowling"],
  "phone": ["0851330885", "0851442889", "0452228965"],
  "email": ["md@gmail.com", "jc@gmail.com", "kd@gmail.com"],
  "company": ["Expert", "Hospital", "Microsoft"]
}

print("\nWelcome to your contact book. Please pick an option below.")

while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact\n 6.Exit\n Enter your choice: "))
    if choice == 1:
        contact["name"].append(input("Please Enter Contact Name: \n"))
        contact["phone"].append(input("Please Enter Phone Number: \n"))
        contact["name"].append(input("Please Enter Email Address: \n"))
        contact["name"].append(input("Please Enter Company Info: \n"))
        print("... Contact Book Updating...\n")

        contact_sheet.append_row(contact)





def add_contact(name, phone_no, email_address, company, worksheet):
    print(f"Updating Contact Book...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(name, phone_no, email_address, company,)
    print(f'{worksheet} worksheet updated successfully\n')

add_contact(name, phone_no, email_address, company, worksheet)