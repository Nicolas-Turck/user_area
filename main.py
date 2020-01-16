from model.connection import *
from view.display import *
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

        """if user_choice == "c":
            print("og")"""
