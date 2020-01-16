from model.connec_account import *
class Verify():
    def __init__(self):
        pass

    def check_pseudo(p, pseudo):

        for row in p :
            for i in row:
                if pseudo== i :
                    print("yes")
                else:
                    print("no")
