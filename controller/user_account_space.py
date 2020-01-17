import sys
from model.delete_account import *
class Display():
    """class for all display of the program"""

    def __init__(self, pseudo):
        self.pseudo = pseudo


    def show_inf(self):
        choice=""

        while choice != "q":
            choice = input(" welcomme to your account \n"
            " (d) for delete account\n"
            " (c) for change data\n"
            " (q) for exit :")
            if choice == "q":
                print("good bye")
                sys.exit()
            if choice == "d":
                user_choice = Delete(self.pseudo)
                user_choice.del_account()
                print("delete")
            if choice =="c":
                print("change data")






