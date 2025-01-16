import random
import pymysql
from logging import exception

try:
    db = pymysql.connect(host="localhost", user="root", passwd="m9r19db", database="Accounts")
    cursor = db.cursor()
except exception():
    print("error occurred connecting to db")


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

def createAccount(accounts):
    print("\n\n" + 10 * " " + 16 * "=")
    print(10 * " " + "ACCOUNT CREATION")
    print(10 * " " + 16 * "=")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Create a strong password: ")
    confPass = input("Confirm your password: ")

    if password == confPass:
        passwordHint = input("Create a password hint incase you ever forget your password: ")
        accountNumber = genAccountNo()
        #accounts[accountNumber] = {'Firstname':fname,'Lastname':lname, 'email':email, 'password':password, 'passwordHint':passwordHint}
        print(f"\n\nYour Account number is {accountNumber}")

        for i,j in accounts[accountNumber].items():
            print(i, j)
        print("\nAccount created successfully!!")


class Accounts:
    def __init__(self,fname, lname, email, accountNo, password, passwordHint, balance = 0):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.accountNo = accountNo
        self.password = password
        self.passwordHint = passwordHint
        self.balance = balance

    def __str__(self):
        return f"accountNo:{self.accountNo}, fname:{self.fname}, lname:{self.lname}, email:{self.email}"

    def comp(self, other):
        b1 = self.balance
        b2 = other.balance
        if b1 > b2:
            return True
        else:
            return False

    def displayAll(self):
        cursor.execute("select * from customer")
        for i in cursor:
            print(i)

def accountLogin():
    global accounts
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
        global choice
        choice = mainMenu()
        next(choice)
    else:
        authentication(count + 1)

def loginMenu():
    pass

def next(choice):
    pass

class DB:
    def __init__(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS Accounts (accountnumber INT(12) PRIMARY KEY, firstname VARCHAR(40),lastname VARCHAR(40),password VARCHAR(40), passwordHint VARCHAR(100), email VARCHAR(30), balance VARCHAR(16))")
        db.commit()

    def insert(self):
        cursor.execute("INSERT INTO customer (accountNumber, firstName,lastName,password,passwordHint, balance) VALUES (%s,%s,%s,%s,%s,%s)",(1234567,'name', 'name', 'password', 'password', 123456))
        db.commit()


