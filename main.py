from BMSmods import *
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
db = pymysql.connect(host="localhost",user="root",passwd="m9r19db",database="Accounts")
mycursor = db.cursor()
admin = {'name':'admin'}
mycursor.execute("INSERT INTO customer (accountNumber, firstName,lastName,password,passwordHint, balance) VALUES (%s,%s,%s,%s,%s,%s)",(1234567,admin['name'],admin['name'],'password','password',123456))
mycursor.execute("select * from customer")
db.commit()


for i in mycursor:
    print(i)


'''For console application,
GUI not present to control flow. hence use of loops and pages'''

'''
IMPLEMENTATOIN USING OOP CONCEPTS
Every account will be a class
Every account will contain a username, account number, email address, password, password hint and balance
The necessary implementations on accounts will be performed using methods
Every page could be a class
'''

def main():
    mainMenu()

if __name__ == '__main__':
    main()