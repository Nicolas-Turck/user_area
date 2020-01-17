## User space
# exercices for use python with bdd
The application has the following features:
- A home page, which allows the user to choose between logging in with an existing account or creating an account
- To create an account, the user has access to a series of prompts requesting the necessary information. 
Once the information has been entered, it is saved in the database.
- If the username or email entered by the user is already taken, we ask the user to enter a new one
- To log in, the user must enter the username and password chosen when creating the account. 
If the credentials are correct, the user then accesses his profile page, otherwise he is shown an error message.
- On his profile page the user can choose to delete his account, his information is then deleted from the database. 
He can also choose to update information by indicating the column to modify and its new value
- The user can exit the application at any time by typing a command of your choice
Technical specifications :
- Passwords are encrypted in a database, in other words they are not stored in clear, 
they are illegible by a human being
This database will contain only one table: users, whose structure is as follows.

-id (integer, serial primary key, not nul)
-name (varchar(50), not nul) 
-firstname (varchar(50), not nul) 
-pseudo (varchar(50), unique, not nul) 
-email (varchar(250), unique, not nul) 
-age (integer, not nul)
-password (varchar  min(64), not nul)
