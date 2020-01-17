from model.connec_account import *
from view.display import *
class Verify():
    def __init__(self, p, pseudo, pwd, password):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = None
        self.password_ok = None

    def check_pseudo(self, p, pseudo, pseudo_ok):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True
                    #Verify.check_password(self.pwd, self.password, self.pseudo_ok, self.password_ok)

    def check_password(self, pwd, password, pseudo_ok):
        """method for verify password if password entry is the
        same of the password corresponding in the database"""
        for row in self.pwd:
            for i in row:
                if self.password == i:
                    self.password_ok = True
                    #Verify.check_password_pseudo(self.pseudo_ok, self.password_ok)

    def check_password_pseudo(self, ):
        """method for verify if pseudo is ok and password ok """
        print(self.password_ok, self.pseudo_ok)
        if self.pseudo_ok == True and self.password_ok == True:
            print("yes")
            space = Display()
            space.show_menu()
        else:
            return





