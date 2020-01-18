class Verify_pseudo_email():
    """class for verify pseudo and email after create account
    if pseudo and email is not in account registered in bdd"""
    def __init__(self):
        self.pseudo = pseudo
        self.verif = verif
        self.verify = verify
        self.email = email




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
