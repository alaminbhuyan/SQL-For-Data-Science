import sys
from dbhelper import DBconnector


class Flipkart:
    info = 0

    def __init__(self):
        # Connect to the database
        self.db = DBconnector()
        self.menu()

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
        self.info = int(data[0][0])
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
            pass
        elif userInput == '2':
            response = self.db.deleteUser(userId=self.info)
            print("Account deleted") if response else print("Opps! Error Occurred to delete account")
            self.menu()
        else:
            sys.exit()

    # def __deleteAccount(self, userId):
    #     print(userId)


if __name__ == "__main__":
    obj = Flipkart()
