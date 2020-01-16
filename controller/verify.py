from model.connec_account import *
class Verify():
    def __init__(self, p, pseudo, pwd, password, pseudo_ok, password_ok):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = pseudo_ok
        self.password_ok = password_ok

    def check_pseudo(self, p, pseudo, pseudo_ok):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        #print(self.p)
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True
                    return self.pseudo_ok


                    print("yes")


    def check_password(self, pwd, password, password_ok):
        """method for verify password"""
        #print(self.pwd)
        for row in self.pwd:
            for i in row:
                if self.password == i:
                    self.pseudo_ok = True
                    return self.pseudo_ok
                    #print(pwd)
                    print("yes")
                    #else:
                        #print("no")

