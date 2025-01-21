from BMSmods import *


def main():
    global page
    page = mainMenu()

    try:
        if int(page) == 1:
            page = createAccount()
            next(page)
        elif int(page) == 2:
            page = accountLogin()
            next(page)
        elif int(page) == 3:
            pass  # exit application
    except ValueError:
        pass

if __name__ == '__main__':
    main()