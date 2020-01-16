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



