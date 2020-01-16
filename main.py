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
    while user_choice != "q":
        user_choice = input ("choice (c) to connect at your account or (w) for create an account:")
        if user_choice == "w":
            choice = Create()
            choice.create_user()

        if user_choice == "c":
            pseudo_ok=False
            password_ok=False
            while pseudo_ok == False and password_ok == False:
                choice = Connect(pseudo_ok, password_ok)
                choice.connect_user()
                if pseudo_ok == True and password_ok == True:



