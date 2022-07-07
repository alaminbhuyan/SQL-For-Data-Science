import mysql.connector
import sys


class DBconnector:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='campusx')
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print("Some Error is occurred. Could not connected to database", e.__class__)
            sys.exit(0)
        else:
            print("Successfully connected")

    def register(self, name: str, email: str, password: str):
        try:
            myquery = """ INSERT INTO users(name, email, password) VALUES(%s ,%s, %s) """
            val = (name, email, password)
            self.mycursor.execute(myquery, val)
            self.conn.commit()
        except:
            return -1
            # return f"Opps! Error Occurred. {e.__class__}"
        else:
            return 1
            # return f"{self.mycursor.rowcount} record inserted successfully"

    def search(self, email:str, password:str):
        try:
            myquery = """ SELECT * FROM users WHERE email = (%s) and password = (%s) """
            val = (email, password)
            self.mycursor.execute(myquery, val)
            data = self.mycursor.fetchall()
        except:
            return -1
        else:
            return data

    def deleteUser(self, userId):
        try:
            myquery = """ DELETE FROM users WHERE id = (%s) """
            val = (userId,)
            self.mycursor.execute(myquery, val)
            self.conn.commit()
        except:
            return -1
        else:
            return 1