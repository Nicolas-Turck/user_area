from model.create_account import *
class Verify_pseudo_email():
    """class for verify pseudo and email after create account
    if pseudo and email is not in account registered in bdd"""
    def __init__(self, pseudo, verify_pseudo, verify, email):
        self.pseudo = pseudo
        self.verify_pseudo = verify_pseudo
        self.verify = verify
        self.email = email
        self.pseudo_ok = None
        self.email_ok = False
        self.email_pseudo = False






    def verify_email(self,verify, email):

        for row in self.verify:
            for i in row:
                if self.email == i:
                    print("email already exist")
                    #return False
                    break

                else:
                    self.email_ok = True
                    return self.email_ok

                    #verify.verify_pseudo(self.pseudo, self.verif, self.email_ok)

    def verif_pseudo(self, verify_pseudo,  pseudo):

        for row in self.verify_pseudo:
            for i in row:
                if self.pseudo == i:
                    #print("pseudo or email already exist")
                    #return False
                    break
                else:

                    self.pseudo_ok =True
                    return self.pseudo_ok

    def check_email_pseudo(self, pseudo_ok, email_ok, create):
        """method for verify if pseudo is ok and password ok """
        try:
            if self.email_ok == True and self.pseudo_ok == True:
                print(" create account")


                #create = True

                #return create

                #Create.create.continue_create(self.pseudo, self.email)

                #space = Display(self.pseudo)
                #space.show_inf()
        except ValueError:
            print("pseudo or email already exist")
            #create = False
            return


