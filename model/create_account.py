from model.connection import *
from controller.verify import *
from controller.verify_pseudo_email import *
import hashlib
from os import *
class Create():
    """class for user create an account
    with is entry adding in bdd if account doesn't  exist"""
    def __init__(self):
        self.choice = connection()
        self.create = connection()
        self.name = None
        self.first = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None
        self.verify_pseudo = None
        self.verify = None
        self.pseudo_ok = False
        self.email_ok = False

    def create_user(self):
        """method for create user account after register entry in attributes
         and add this attributes in bdd """
        create = False
        self.choice.initialize_connection()
        self.name = input("enter name:")
        self.first = input("enter firstname:")
        self.pseudo = input("enter pseudo:")
        self.email = input("enter your email adress:")
        self.age = input("enter your age:")
        self.password = input("create your password:")
        self.choice.cursor.execute("SELECT pseudo  FROM users;")
        self.verify_pseudo = self.choice.cursor.fetchall()
        self.choice.cursor.execute("SELECT email  FROM users;")
        self.verify = self.choice.cursor.fetchall()
        verify = Verify_pseudo_email(self.pseudo, self.email, self.verify_pseudo, self.verify)
        verify.verify_email(self.email, self.verify)
        verify.verif_pseudo(self.verify_pseudo, self.pseudo)
        verify.check_email_pseudo(self.pseudo_ok, self.email_ok, create)

        if create == True:
            self.choice.initialize_connection()
            self.password = hashlib.sha256(self.password.encode()).hexdigest()
            self.choice.cursor.execute("INSERT INTO users(name, firstname, pseudo, email, age, password) VALUES "
                                       "(%s, %s, %s, %s, %s, %s);",(self.name, self.first, self.pseudo, self.email, self.age, self.password))
            self.choice.connection.commit()
            self.choice.close_connection()
            system('clear')
