import random
import pymysql
from logging import exception


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
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Create a strong password: ")
    confPass = input("Confirm your password: ")

    if password == confPass:
        passwordHint = input("Create a password hint incase you ever forget your password: ")
        Accounts.startDB()
        accountNumber = Accounts.checkAccountNo(genAccountNo())
        global customer
        customer = Accounts(fname, lname, email,password, passwordHint,accountNumber)
        print("\nAccount created successfully!!\n")
        print(customer)
        return 2

class Accounts:
    def __init__(self,fname, lname, email, password, passwordHint,accountNumber):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.accountNo = accountNumber
        self.password = password
        self.passwordHint = passwordHint
        self.balance = 0
        self.update()

    def __str__(self):
        return f"accountNo:{self.accountNo}, fname:{self.fname}, lname:{self.lname}, email:{self.email}"

    def comp(self, other):
        b1 = self.balance
        b2 = other.balance
        if b1 > b2:
            return True
        else:
            return False

    @staticmethod
    def displayAll():
        cursor.execute("select * from Accounts")
        for i in cursor:
            print(i)

    @staticmethod
    def startDB():
        global db, cursor
        try:
            db = pymysql.connect(host="localhost", user="root", passwd="m9r19db", database="Accounts")
            cursor = db.cursor()
        except pymysql.err.InternalError:
            print("error occurred connecting to db")
        except pymysql.err.DatabaseError:
            print("error occurred connecting to db")
        finally:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS Accounts (accountnumber INT(12) PRIMARY KEY, firstname VARCHAR(40),lastname VARCHAR(40),password VARCHAR(40), passwordHint VARCHAR(100), email VARCHAR(30), balance VARCHAR(16))")

    @staticmethod
    def checkAccountNo(accountNo):
        cursor.execute("SELECT 1 from Accounts WHERE accountnumber = %s LIMIT 1",(accountNo))
        result = cursor.fetchone()
        if result:
            Accounts.checkAccountNo(accountNo = genAccountNo())
        else:
            return accountNo

    def update(self):
        cursor.execute(
            "INSERT INTO Accounts (accountNumber, firstName,lastName,password,passwordHint,email, balance) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (self.accountNo, self.fname, self.lname, self.password, self.passwordHint, self.email, self.balance))
        db.commit()

def accountLogin():
    global accounts
    print("\n\n" + 10 * " " + 13 * "=")
    print(10 * " " + "ACCOUNT LOGIN")
    print(10 * " " + 13 * "=")
    authentication()
    loginMenu()

def authentication(count=0):
    accountNumber = int(input("\nEnter your account number: "))
    password = input("Enter your password: ")
    if accounts[accountNumber]['password'] == password:
        loginMenu()
    elif count == 3:
        global page
        page = mainMenu()
        next(page)
    else:
        authentication(count + 1)

def loginMenu():
    pass

def next(choice):

    if choice == 1:
        createAccount()
    elif choice == 2:
        accountLogin()
    elif choice == 3:
        pass #exit application
