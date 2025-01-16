from logging import exception

from BMSmods import *


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