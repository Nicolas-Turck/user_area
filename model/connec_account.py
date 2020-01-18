from model.connection import *
import hashlib
from getpass import *
from controller.verify import *
from controller.verify import *
from os import *
class Connect:
    """class for ask pseudo and passwor if user
    choice connect to user account"""
    def __init__(self):
        self.choice = connection()
        self.pseudo = None
        self.password = None
        self.p = None
        self.pwd = None
        self.count = None
        self.pseudo_ok = None
        self.password_ok = None
        self.pseudo_password = False

    def connect_user(self):
        """method for ask pseudo and password and
         and return of bdd list pseudo and list password after verify
          in new method if entry is in list pseudo and password """
        self.choice.initialize_connection()
        self.pseudo = input("enter PSEUDO :")
        self.password = getpass()
        system('clear')
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        self.choice.cursor.execute("SELECT pseudo FROM users;")
        self.p = self.choice.cursor.fetchall()
        self.choice.cursor.execute("SELECT password FROM users;")
        self.pwd = self.choice.cursor.fetchall()
        a = Verify(self.p, self.pseudo, self.pwd, self.password)
        a.check_pseudo(self.p, self.pseudo,self.pseudo_ok)
        a.check_password(self.pwd, self.password, self.password_ok)
        a.check_password_pseudo(self.pseudo)























