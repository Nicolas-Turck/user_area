from model.connec_account import *
class Verify():
    def __init__(self, p, pseudo, pwd, password):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password

    def check_pseudo(self, p, pseudo):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        #print(self.p)
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    #print(p)
                    print("yes")
                    #else:
                        #print("no")



    def check_password(self, pwd, password):
        """method for verify password"""
        #print(self.pwd)
        for row in self.pwd:
            for i in row:
                if self.password == i:
                    #print(pwd)
                    print("yes")
                    #else:
                        #print("no")

