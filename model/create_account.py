from model.connection import *
class Create:
    """class for user create an account if not exist"""
    def __init__(self):

        self.choice = connection()

    def create_user(self, name, first, pseudo, email, age, password):
        """method for create user account"""
        self.choice.initialize_connection()

        self.choice.cursor.execute("INSERT INTO message(name, firstname, pseudo, email, age, password) VALUES "
                                   "(%s, %s, %s, %s, %s, %s);",(name, first, pseudo, email, age, password))
        self.choice.connection.commit()
        self.choice.close_connection()
