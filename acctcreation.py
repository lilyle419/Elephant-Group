import sys
from argparse import ArgumentParser
import hashlib
import base64
import uuid
import string
import random

sym = "!@$%^&*()-+]#"
letters = string.ascii_letters
numbers = string.digits

class acctcreation():
    """Class where users are prompted for a login to acceess their bank account

        Attributes:
            userinfo: a dictionary of users information
    
    """
    
    
    def __init__(self, filepath):
        """Opens file and populates dictionary

        Args:
            self
            filepath (string): the desired input file as a string
        
        Side effects:
            populates dictionary

        """
        self.userinfo = {}
        
        with open(filepath, 'r', encoding = "utf-8") as new_file:
            for line in new_file:
                user = line.strip().split(",")

                #salt and hash password here
                #salt = uuid.uuid4().hex
                #hashedpass = hashlib.sha256(user[1].encode('utf-8') + salt.encode('utf-8')).hexdigest()

                self.userinfo[user[0]] = (user[1], user[2], float(user[3])) #key:username  tuple: salt, hashedpass, money

    
    
    def create_acct(self):
        """Allows users to create their bank account

            Side effects:
                adds a new account to the database
        
        """   
        created_account = False
        while (created_account is False):
            username = input("Enter your desired username:")
            pass1 = input("Enter your desired password\nPassword must have a special character, a number, and a capital number:\n")
            pass2 = input("Confirm your desired password:")
            if pass1 == pass2:
                password = pass1
                print("Checking password security")
                
                if self.check_password(password) == True:
                    created_account = True
                    print("Password secure!")

                    deposit = input("Please deposit any initial funds or put 0 if you so choose:")
                    # TODO check if input is number 

                    #salt and hash password here and then store it to the database with the funds
                    salt = uuid.uuid4().hex
                    hashedpass = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

                    self.userinfo[username] = (salt, hashedpass, float(deposit)) #key:username  tuple: salt, hashedpass, money

                
                else:
                    print("Password not secure, generating secure password")
                    # TODO insert password.py related code here
 
            
            else:
                print("Passwords do not match. Please try again")
        

        print("exiting account creation, line 80")

    def check_password(self, password):
        password_good = False
        has_char = False
        has_num = False
        has_capital = False
        char_list = ["!", "@", "#", "$", "%", "&", "*", "?"]
        num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        capital_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        for char in char_list:
            if char in password:
                has_char = True
        
        for number in num_list:
            if number in password:
                has_num = True
        
        for letter in capital_list:
            if letter in password:
                has_capital = True
        
        if ((has_char == True) & (has_num == True) & (has_capital == True)):
            password_good = True

        return password_good


    #TODO
    def add_money(self,user, money):    
        print("adding money")

    def take_money(self,user, money):
        print("subtracting money")

    def get_balance(self, name):
        """ returns the user's balance
        
        Args:
            name: the user's username
        """
        return 0


    def add_user(self, user):
        """ adds a user to the catalog
        
        Args:
            user (user class): an instance of the user class

        """

        return






"""      
def main(filepath):
   start = Login(filepath)
   start.login_attempt()


if __name__ == "__main__":
    main("startinguserdata.csv")

"""
