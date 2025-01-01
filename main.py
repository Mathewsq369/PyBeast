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


def mainMenu():
    print(13 * "=")
    print(3 * " " + "WELCOME")
    print(13 * "=")
    print("\nChoose option you want to perform")
    print("1. CREATE ACCOUNT")
    print("2. ACCOUNT LOGIN")
    print("3. EXIT APLICATION")
    choice = int(input("Input choice >> "))
    return choice

mainMenu()