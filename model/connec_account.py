from model.connection import *
import hashlib
from getpass import *
from controller.verify import *
from controller.verify import *
class Connect:
    """class for connect to user account"""
    def __init__(self):
        self.choice = connection()
        self.pseudo = None
        self.password = None
        self.p = None
        self.pwd = None
        self.count = None
        self.pseudo_ok = False
        self.password_ok = False

    def connect_user(self):
        self.choice.initialize_connection()
        self.pseudo = input("enter PSEUDO :")
        self.password = getpass()
        self.password = hashlib.sha256(b'').hexdigest()
        self.choice.cursor.execute("SELECT pseudo FROM users;")
        self.p = self.choice.cursor.fetchall()
        self.choice.cursor.execute("SELECT password FROM users;")
        self.pwd = self.choice.cursor.fetchall()
        a = Verify(self.p, self.pseudo, self.pwd, self.password)
        a.check_pseudo(self.p, self.pseudo)
        a.check_password(self.pwd, self.password)

        #self.password = getpass()
        #self.choice.cursor.executed("SELECT password FROM users;")
        #self.pwd = self.choice.cursor.fetchall()
        #b = Verify(self.pwd, self.password)
        #b.check_password(self.pwd, self.password)

















