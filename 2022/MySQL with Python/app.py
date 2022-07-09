import sys
from dbhelper import DBconnector


class Flipkart:

    def __init__(self):
        # Connect to the database
        self.db = DBconnector()
        self.menu()
        self.__userId = 0

    def menu(self):
        user_input = input("""
        1. Enter 1 to register: 
        2. Enter 2 to LogIn: 
        3. Press 'q' to exit: 
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        response = self.db.register(name=name, email=email, password=password)
        if response:
            print(f"{self.db.mycursor.rowcount} record are inserted successfully")
        else:
            print("Opps! Some error is occurred")

        self.menu()

    def login(self):
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        data = self.db.search(email=email, password=password)
        self.__userId = int(data[0][0])
        if len(data) == 0:
            print("Incorrect Email/Password")
            self.login()
        else:
            print("Successfully LogIn!!")
            # It returns list of tuple
            print(f"Username: {data[0][1]}, User-Email: {data[0][2]}, User Password: {data[0][3]}")
            self.userProfile()

    def userProfile(self):
        userInput = input("""
        1. Update your profile
        2. Delete your account
        3. Press 'q' to exit()
        """)
        if userInput == '1':
            self.__updateInfo()
        elif userInput == '2':
            response = self.db.deleteUser(userId=self.__userId)
            print("Account deleted") if response else print("Opps! Error Occurred to delete account")
            self.menu()
        else:
            sys.exit()

    def __updateInfo(self):
        userInput = input("""
        Tell me which information do you wanna update? Ex. name,email,password...
        Press 'q' to quit.
        """).split(',')

        if 'name' and 'email' and 'password' in userInput:
            uname, uemail, upass = input("Enter your name, email, and password: ").split(',')
            response = self.db.updateAll(self.__userId, uname, uemail, upass)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'name' and 'email' in userInput:
            uname, uemail = input("Enter your name, email: ").split(',')
            response = self.db.update_name_email(self.__userId, uname, uemail)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'name' and 'password' in userInput:
            uname, upass = input("Enter your name, email: ").split(',')
            response = self.db.update_name_pass(self.__userId, uname, upass)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'email' and 'password' in userInput:
            uemail, upass = input("Enter your name, email: ").split(',')
            response = self.db.update_email_pass(self.__userId, uemail, upass)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'name' in userInput:
            uname = input("Enter your name, email: ")
            response = self.db.update_name(self.__userId, uname)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'email' in userInput:
            uemail = input("Enter your name, email: ")
            response = self.db.update_email(self.__userId, uemail)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        elif 'password' in userInput:
            upass = input("Enter your name, email: ")
            response = self.db.update_pass(self.__userId, upass)
            if response:
                print(f"Successfully {self.db.mycursor.rowcount} record is updated!!!")
            else:
                print("Opps!! Some error is occurred")
        else:
            sys.exit()


if __name__ == "__main__":
    obj = Flipkart()
