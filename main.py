"""
recoding the bank account management system
"""

"""
After starting the system
1. User wants to login
2. User wants to create account
3.Exit 
"""

'''
could im[lement accounts as classes
'''
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
from BMSmods import *
admin = {'name':'Admin', 'password': 'password'}
accounts = {1234567:admin}


'''For console application,
GUI not present to control flow. hence use of loops and pages'''

'''
IMPLEMENTATOIN USING OOP CONCEPTS
Every account will be a class
Every account will contain a username, account number, password, password hint and balance
The necessary implementations on accounts will be performed using methods
Every page could be a class
'''

def main():
    mainMenu()

if __name__ == '__main__':
    main()