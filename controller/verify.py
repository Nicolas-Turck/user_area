from model.connec_account import *
class Verify():
    def __init__(self, p, pseudo, pwd, password):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = False
        self.password_ok = False

    def check_pseudo(self, p, pseudo):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True
                    #Verify.check_password(self.pwd, self.password, self.pseudo_ok)
                    return self.pseudo_ok

    def check_password(pwd, password, password_ok):
        """method for verify password if password entry is the
        same of the password corresponding in the database"""
        for row in pwd:
            for i in row:
                if password == i:
                    password_ok = True


    def check_password_pseudo(self):
        if pseudo_ok == True and password_ok == True:
            ac = True
            print(password_ok, pseudo_ok)
            print("yes")
            return ac



