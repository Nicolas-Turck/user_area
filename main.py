from model.connection import *
from view.display import *
"""test for verify if connect to bbd is ok """
test = connection()
test.initialize_connection()
test.close_connection()

if __name__=='__main__':

