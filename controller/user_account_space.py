import sys
from model.delete_account import *
from model.change_data import *
from os import *
class Display():
    """class for display menu  of user account"""
    def __init__(self, pseudo):
        self.pseudo = pseudo

    def show_inf(self):
        """method for got to class corresponding of user choice"""
        choice = ""
        while choice != "q":
            choice = input(" welcomme to your account \n"
            " (d) for delete account\n"
            " (c) for change data\n"
            " (q) for exit :")
            if choice == "q":
                print("good bye")
                sys.exit()
            if choice == "d":
                system('clear')
                user_choice = Delete(self.pseudo)
                user_choice.del_account()

            if choice =="c":
                system('clear')
                user_choice = Change(self.pseudo)
                user_choice.change_datta()







