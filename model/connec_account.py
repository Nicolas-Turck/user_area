from model.connection import *
import hashlib
from getpass import *
from controller.verify import *

class Connect:
    """"""
    def __init__(self):
        self.choice = connection()
        self.pseudo = None
        self.password = None
        self.p = None

    def connect_user(self):
        self.choice.initialize_connection()
        self.pseudo = input("enter PSEUDO :")
        self.choice.cursor.execute("SELECT pseudo FROM users;")
        self.p = self.choice.cursor.fetchall()
        Verify.check_pseudo(self.p, self.pseudo)
















