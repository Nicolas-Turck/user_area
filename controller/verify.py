from model.connec_account import *
from controller.user_account_space import *
from model.create_account import *
"""class for test entry of user and go to account if entry is ok
ok return if entry is not ok"""
class Verify():
    def __init__(self, p, pseudo, pwd, password, verif, verify, email):
        self.p = p
        self.pseudo = pseudo
        self.verif = verif
        self.verify = verify
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = None
        self.password_ok = None

    def check_pseudo(self, p, pseudo, pseudo_ok):
        """method for verify if pseudo entry is in
        bdd in champ pseudo"""
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True

    def check_password(self, pwd, password, pseudo_ok):
        """method for verify password if password entry is the
        same of the password corresponding in the database"""
        for row in self.pwd:
            for i in row:
                if self.password == i:
                    self.password_ok = True

    def check_password_pseudo(self, pseudo):
        """method for verify if pseudo is ok and password ok """
        if self.pseudo_ok == True and self.password_ok == True:
            print("account found")
            space = Display(self.pseudo)
            space.show_inf()
        else:
            print("account not found")
            return

    def verify_email(self, verif, verify, email, pseudo):
        try:
            for row in self.verify:
                for i in row:
                    if self.email == i:
                        return False
        except:
            return True
                        #Verify.verify_pseudo(pseudo, verif)

    def verify_pseudo(self, verif,  pseudo):
        try:
            for row in self.verif:
                for i in row:
                    if self.pseudo == i:
                        return False
        except:
            return True















