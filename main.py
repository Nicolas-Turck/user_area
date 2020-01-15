from model.connection import *
from view.display import *
"""test for verify if connect to bbd is ok """
test = connection()
test.initialize_connection()
test.close_connection()

if __name__=='__main__':
    choice = ""
    while choice not in ["c", "w"]:
        choice = input ("choice (c) to connect at your account or (w) for create an account:")
        if choice == "c":
            print("go")
        if choice == "w":
            print("og")
