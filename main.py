from model.connection import *
from view.display import *
from model.connec_account import *
from model.create_account import *
from controller.verify import *
"""test for verify if connect to bbd is ok """
test = connection()
test.initialize_connection()
test.close_connection()

if __name__=='__main__':
    user_choice = ""

    while user_choice != "q":
        user_choice = input("choice (c) to connect at your account or (w) for create an account:")
        if user_choice == "w":
            choice = Create()
            choice.create_user()

        if user_choice == "c":
            ac = False
            while ac == False:
                choice = Connect()
                choice.connect_user()
                print(ac)
                if ac == True:
                    print("id user ok")
                    space = Display()
                    space.show_menu()
                else:
                    print("not entry ")



