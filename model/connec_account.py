from model.connection import *
import hashlib
from getpass import *

class Connect:
    """"""
    def __init__(self):
        self.choice = connection()
        self.pseudo = None
        self.password = None

    def connect_user(self):
        self.choice.initialize_connection()
        self.pseudo = input("enter PSEUDO :")
        self.password = getpass()
        self.choice.cursor.execute("SELECT pseudo, password FROM users;")
        list = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return list

    def check_if_found(self):





