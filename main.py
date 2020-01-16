from model.connection import *
from view.display import *
from model.connec_account import *
from model.create_account import *
"""test for verify if connect to bbd is ok """
test = connection()
test.initialize_connection()
test.close_connection()

if __name__=='__main__':
    user_choice = ""
    pseudo_password = False
    pseudo_ok = False
    password_ok = False
    #password_ok = False
    while user_choice != "q":
        user_choice = input ("choice (c) to connect at your account or (w) for create an account:")
        if user_choice == "w":
            choice = Create()
            choice.create_user()

        if user_choice == "c":
            while pseudo_ok ==False and password_ok == False :
                choice = Connect()
                choice.connect_user(pseudo_password)
                print(pseudo_password)
                if  pseudo_ok == True and passwor_ok == True:
                    space = Display()
                    space.show_menu()



