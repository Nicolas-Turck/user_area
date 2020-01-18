from model.connection import *
from os import *
import sys
class Delete():
    """class for user delete this account"""
    def __init__(self, pseudo):
        self.user_choice = connection()
        self.pseudo = pseudo

    def del_account(self):
        """"method for delte user account after connect to bdd"""
        confirm = input("delete account y/n:")
        if confirm == "y":
            self.user_choice.initialize_connection()
            self.user_choice.cursor.execute("DELETE FROM users WHERE pseudo = %s;", (self.pseudo,))
            self.user_choice.connection.commit()
            self.user_choice.close_connection()
            print("account deleted good bye")
            #system('clear')
            sys.exit()
        else:
            system('clear')
            return
