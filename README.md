# Contact Book

For this project my objective was to create an interactive contact book application where a user can access their contacts on the go. To do this I linked my application to a Google sheet so that user input is pushed to the Google sheet and can be accessed anywhere.

# User Stories

## User Goals

"As a user, I want to be able to fully control my contacts in an application so that I can access them from wherever I am"

- To be able to access contacts easily
- To be able to add new contacts easily
- To be able to search for contacts
- To be able to delete contacts 
- To be able to access contacts from anywhere

# Features

### Main Menu
The main menu shows when a user first runs the programme. It lists 5 options and asks a user for input for what they would like to do. This menu fires again after a task has been completed so a user can choose another option or exit the programme.

![main menu screen](/documentation/main.png)

### Show Contacts
This shows the user their full list of contacts displayed in an easy to read formatted table, read directly from the attached Google sheet, meaning it will always be up to date.

![contacts being displayed](/documentation/view-contacts.png)

### Add Contact
The add contact function takes user input for name, phone number, email and address and updates the Google sheet with this information. The name input automatically changes the name to a lower case string for better search functionality.

![add contact inputs](/documentation/add-contact.png)

### Search Contact
This takes user input to search the Google sheet for the name of the contact and returns the contact information to the terminal. The input is also changed to a lower case string meaning any name that matches will show up and not be case sensitive.

![contact being searched and displayed](/documentation/search-contact.png)

### Delete Contact
This takes user input for a name to delete from contacts. If the name is found the corresponding contact is deleted from the Google sheet, if not an error appears to the user.

![contact being deleted](/documentation/delete.png)

### Exit
This ends the loop and exits the programme.

# Data Model
The way I structured this project was to define a number of functions for the different tasks a user needed, then run a while loop for the main function of the programme. While this returned true the questions where asked to the user and input was taken to update contact book. When the exit option is picked the while loop breaks and exits the programme.

I used the gspread library in python and imported my Google sheet credentials to link the Google sheet to the programme. I had also used the pandas library for certain functions but when this gave me bugs I removed it from the programme and found a different way to display info. Later on in the development of my project I added the art library to print 'Contact Book' in large writing at the start of the main menu. I liked the look this gave my programme.

Although a class can be used to create a contact book in python I didn't think it was needed my intended use and the way I had planned to execute this idea. I planned out the flow of my programme using a flow chart seen below. After each function is executed the main menu shows again until the loop is broken using the exit command. 

![Flow chart](/documentation/flow-chart.png)

# Testing and Validating
To test my python code I passed it through the PEP8 code validator and received no errors

![python code validator](/documentation/python-validator.png)

### Manual Testing 
To test my project I ran the programme and inputted a number of strings and integers to test how the programme handles information and if my error messages worked as expected

### Bugs
- One bug I came across was that when I added a contact then went to view all contacts the one I had just added did not display. I fixed this by changing the method in which I showed the contacts. I was using the pandas library to show contact but after I found this bug I switched the way in which this function ran and my problem was fixed
- Another problem I came across was when searching for a contact was that the name was case sensitive. This took me a while to figure out but was an easy fix in the end as I just converted all strings to lower case when entered, this fixed my problem

### Remaining Bugs
- No remaining bugs

# Deployment & Local Deployment

## Deployment
This project was deployed using Code Institutes mock terminal for Heroku. The steps for deployment are shown below

- First you need to go to Heroku.com and create new app
- Enter an app name and select Europe as your region
- Next go to deploy tab and then to deployment method to authorize and connect my GitHub account
- After successful connection I selected main branch from contact-book repository 
- Then I went to settings and the buildpacks section. I added python and nodejs buildpacks. In that order
- Next step I went to Config Vars and added KEY "CREDS" with the value of my creds.json file in my repository
- I also another key "PORT" with the value "8080" and saved changes
- I then went to the deploy tab and chose automatic deployment
- The link to my deployed site [Contact Book](https://contact-book123.herokuapp.com/)

## Local Development

### How to Fork
1. Log in (or sign up) to Github.
2. Go to the repository for this project, mickdowling16/contact-book
3. Click the Fork button in the top right corner.

### How to Clone
1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, mickdowling16/contact-book
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

# Credits
- I used the help of Stack Overflow to search problems and bugs I was facing with my code
- I used w3schools for help with certain keywords and syntax
- I used Slack to research problems and get advice from threads where people had the same problems as myself. 
- I used [Smart Draw](https://www.smartdraw.com/) for my flow chart 