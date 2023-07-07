#1)database
#2)model
#3)UI
#4)method
from lesson5.Libraryproject.model import User


def register():
    d = {
        "name": input("Name"),
        "username": input("Username"),
        "password": input("Password")
    }
    user = User(**d)
    if user.check_username():
        print("Your username already exists!")
        return
    user.save_user()
    print("Registrated successfully !")

def login():
    pass

def UI():
    while True:
        text = """
        1)Register
        2)Login
        3)exit
            >>>"""
        key = int(input(text))
        match key:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break

UI()