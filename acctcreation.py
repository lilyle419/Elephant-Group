import sys
from argparse import ArgumentParser
import password



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
        print("acctcreation line 28")
        
        with open(filepath, 'r', encoding = "utf-8") as new_file:
            for line in new_file:
                user = line.strip().split(",")
                self.userinfo[user[0]] = (user[1], float(user[2])) #key:username  tuple: password, money in account
    
    
    def create_acct(self):
        """Allows users to create their bank account

            Side effects:
                adds a new account to the database
        
        """   
        created_account = False
        while (created_account is False):
            username = input("Enter your desired username:")
            pass1 = input("Enter your desired password:")
            pass2 = input("Confirm your desired password:")
            if pass1 == pass2:
                password = pass1
                print("Checking password security")
                
                if self.check_password(password) == True:
                    print("Password secure")

                    deposit = input("Please deposit any initial funds or put 0 if you so choose:")

                    #salt and hash password here and then store it to the database with the funds
                
                else:
                    print("Password not secure generating secure password")
                    



                
            
            else:
                print("Passwords do not match. Please try again")

    def check_password(password):
        password_good = False
        has_char = False
        has_num = False
        has_capital = False
        char_list = ["!", "@", "#", "$", "%", "&", "*", "?"]
        num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        capital_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        for char in char_list:
            if password.contains(char):
                has_char = True
        
        for number in num_list:
            if password.contains(char):
                has_num = True
        
        for letter in capital_list:
            if password.contains(char):
                has_capital = True
        
        if ((has_char == True) & (has_num == True) & (has_capital == True)):
            password_good = True

        return password_good
        







"""      
def main(filepath):
   start = Login(filepath)
   start.login_attempt()


if __name__ == "__main__":
    main("startinguserdata.csv")

"""