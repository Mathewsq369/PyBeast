"""
recoding the bank account management system
"""

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
import random
admin = {'name':'Admin', 'password': 'password'}
accounts = {1234567:admin}

def mainMenu():
    print(10 * " " + 13 * "=")
    print(10 * " " + 3 * " " + "WELCOME")
    print(10 * " " + 13 * "=")
    print("\nChoose option you want to perform")
    print("1. CREATE ACCOUNT")
    print("2. ACCOUNT LOGIN")
    print("3. EXIT APPLICATION")
    choice = int(input("Input choice >> "))
    return choice

def genAccountNo():
    a = random.randint(12344321, 87654321)
    return a

def createAccount():
    print("\n\n" + 10 * " " + 16 * "=")
    print(10 * " " + "ACCOUNT CREATION")
    print(10 * " " + 16 * "=")
    username = input("Enter a username: ")
    email = input("Enter your email address: ")
    password = input("Create a strong password: ")
    confPass = input("Confirm your password: ")

    if password == confPass:
        passwordHint = input("Create a password hint incase you ever forget your password: ")
        accountNumber = genAccountNo()
        accounts[accountNumber] = {'username':username, 'email':email, 'password':password, 'passwordHint':passwordHint}
        print(f"\n\nYour Account number is {accountNumber}")

        for i,j in accounts[accountNumber].items():
            print(i, j)
        print("\nAccount created successfully!!")

def accountLogin():
    login = False
    print("\n\n" + 10 * " " + 13 * "=")
    print(10 * " " + "ACCOUNT LOGIN")
    print(10 * " " + 13 * "=")
    authentication()

def authentication(count=0):
    accountNumber = int(input("\nEnter your account number: "))
    password = input("Enter your password: ")
    if accounts[accountNumber]['password'] == password:
        loginMenu()
    elif count == 3:
        choice = mainMenu()

    else:
        authentication(count + 1)


def loginMenu():
    pass
authentication()
choice = mainMenu()
createAccount()
accountLogin()