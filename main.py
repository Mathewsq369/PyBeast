"""
recoding the bank account management system
"""
import random

"""
After starting the system
1. User wants to login
2. User wants to create account
3.Exit 
"""


"""
for 1
    ask for accountnumber and password
    if password forgotten request for password hint
    failure to remember after the password hint, user should contact customer service
    
for 2
    ask for user information: name, emailaddr
    user creates password and recovery password hint
    account number generated and displayed to the user
    user is redirected to the login page
"""
admin = {'name':'Admin', 'password': 'password'}
accounts = {1234567:admin}

def mainMenu():
    print(10 * " " + 13 * "=")
    print(10 * " " + 3 * " " + "WELCOME")
    print(10 * " " + 13 * "=")
    print("\nChoose option you want to perform")
    print("1. CREATE ACCOUNT")
    print("2. ACCOUNT LOGIN")
    print("3. EXIT APLICATION")
    choice = int(input("Input choice >> "))
    return choice

choice = mainMenu()

def genAccountNo():
    a = random.randint(12344321, 87654321)
    return a

def createAccount():
    username = input("Enter a username: ")
    email = input("Enter your email address: ")
    password = input("Create a strong password: ")
    confPass = input("Confirm your password: ")

    if password == confPass:
        passwordHint = input("Create a password hint incase you ever forget your password: ")
        accountNumber = genAccountNo()
        accounts[accountNumber] = {'username':username, 'email':email, 'password':password, 'passwordHint':passwordHint}
        print(f"Your new Account number is {accountNumber}")

        print(accounts[accountNumber])
        print("Account created successfully")


createAccount()