from logging import exception

from BMSmods import *


db = pymysql.connect(host="localhost",user="root",passwd="m9r19db",database="Accounts")
mycursor = db.cursor()
admin = {'name':'admin'}
mycursor.execute("INSERT INTO customer (accountNumber, firstName,lastName,password,passwordHint, balance) VALUES (%s,%s,%s,%s,%s,%s)",(1234567,admin['name'],admin['name'],'password','password',123456))
db.commit()

mycursor.execute("select * from customer")


for i in mycursor:
    print(i)



def main():
    page = mainMenu()

    try:
        if int(page) == 1:
            createAccount()
        elif int(page) == 2:
            accountLogin()
        elif int(page) == 3:
            pass  # exit application
    except exception():
        pass

if __name__ == '__main__':
    main()