from model.connection import *
import hashlib
from getpass import *

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
        p = self.choice.cursor.fetchall()
        #Connect.check_pseudo(p, self.pseudo)
        """self.password = getpass()
        self.choice.cursor.execute(SELECT password FROM users;)"""

    def check_pseudo(self, p, pseudo):
        if self.pseudo in self.p:
            print("yes")
        else:
            print("no")













