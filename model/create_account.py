from model.connection import *
import hashlib
class Create:
    """class for user create an account if not exist"""
    def __init__(self):
        self.choice = connection()
        self.name = None
        self.first = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None

    def create_user(self):
        """method for create user account"""
        self.choice.initialize_connection()
        self.name = input("enter name:")
        self.first = input("enter firstname:")
        self.pseudo = input("enter pseudo:")
        self.email = input("enter your email adress:")
        self.age = input("enter your age:")
        self.password = input("create your password:")
        self.password = hashlib.sha256(b'').hexdigest()
        self.choice.cursor.execute("INSERT INTO users(name, firstname, pseudo, email, age, password) VALUES "
                                   "(%s, %s, %s, %s, %s, %s);",(self.name, self.first, self.pseudo, self.email, self.age, self.password))
        self.choice.connection.commit()
        self.choice.close_connection()
