from model.connec_account import *
class Verify():
    def __init__(self, p, pseudo, pwd, password):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = False
        self.password_ok = False

    def check_pseudo(self, p, pseudo, pwd, password):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        #print(self.p)
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True
                    print(self.pseudo_ok)
                    Verify.check_password(pwd, password)
                    #return self.pseudo_ok
                    print("yes")

    def check_password(pwd, password):
        """method for verify password if password entry is the same of the password corresponding in the database"""
        print(pwd)
        for row in pwd:
            for i in row:
                if self.password == i:
                    self.password_ok = True
                    print(self.password_ok)
                    return self.pseudo_ok, self.password_ok
                    #print(pwd)
                    print("yes")
                    #else:
                        #print("no")

