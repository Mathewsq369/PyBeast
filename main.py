from logging import exception

from BMSmods import *


def main():
    page = mainMenu()

    try:
        if int(page) == 1:
            global page
            page = createAccount()
            next(page)
        elif int(page) == 2:
            global page
            page = accountLogin()
            next(page)
        elif int(page) == 3:
            global page
            pass  # exit application
    except exception():
        pass

if __name__ == '__main__':
    main()