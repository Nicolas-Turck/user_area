import sys
class Display():
    """class for all display of the program"""

    def __init__(self):
        pass

    def show_inf(self):
        choice=""

        while choice != "q":
            choice = input(" welcomme to your account \n"
            " (d) for delete account\n"
            " (c) for change data\n"
            " (q) for exit :")
            if choice == "q":
                print("good bye")
                sys.exit()
            if choice == "d":
                print("delete")
            if choice =="c":
                print("change data")






