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
        self.pseudo_ok = None
        self.password_ok = None
        self.pseudo_password = False

    def connect_user(self, pseudo_password):
        """method for connect after verify """
        self.choice.initialize_connection()
        self.pseudo = input("enter PSEUDO :")
        self.password = getpass()
        self.password = hashlib.sha256(b'').hexdigest()
        self.choice.cursor.execute("SELECT pseudo FROM users;")
        self.p = self.choice.cursor.fetchall()
        self.choice.cursor.execute("SELECT password FROM users;")
        self.pwd = self.choice.cursor.fetchall()
        a = Verify(self.p, self.pseudo, self.pwd, self.password, self.password, self.password_ok)
        a.check_pseudo(self.p, self.pseudo, self.pseudo_ok)
        a.check_password(self.pwd, self.password, self.password_ok)
        if self.password_ok == True \
                and self.pseudo_ok == True:
            self.pseudo_password = True
            return self.pseudo_password
        else:
            self.pseudo_password = False
            return self.pseudo_password


















