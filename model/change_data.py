from model.connection import *
from os import *


class Change():
    """class for user choice delete this account"""

    def __init__(self, pseudo):
        self.user_choice = connection()
        self.pseudo = pseudo

    def change_datta(self):
        """"method for change data in  this account after connect to bdd"""
        column = ""
        while column not in ['lastname', 'firstname', 'pseudo', 'email', 'age', 'password']:
            column = input("entry champ to change \n[lastname][firstname], [pseudo], [email], [age], [password]")
            datta = input("enter new datta:")
            self.user_choice.initialize_connection()
            self.user_choice.cursor.execute("UPDATE users set " + column + " = %s WHERE pseudo = %s;", (datta, self.pseudo,))
            self.user_choice.connection.commit()
            self.user_choice.close_connection()
            system('clear')
