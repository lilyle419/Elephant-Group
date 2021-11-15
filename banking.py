
import sys
from argparse import ArgumentParser



class Login():
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
                self.userinfo[user[0]] = (user[1], float(user[2])) #key:username  tuple: password, money in account
    
    
    
    def login_attempt(self):
        """Allows users to login to their bank account

            Side effects:
                a succesful login will (eventually) give access to a users bank account
        
        """
        
        good_login = False
        
        while (good_login is False):
            
            username = input("Enter your username:")

            if username in self.userinfo.keys():
                
                password = input("Enter your password:")

                if password in self.userinfo[username]:
                    good_login = True
                    print("Login succesful")
                    #some code to allow them to access their specific account would come after"
                else:
                    print ("Incorrect username or password please try again")
            else:
                print ("Incorrect username or password please try again")


def main(filepath):
   start = Login(filepath)
   start.login_attempt()


if __name__ == "__main__":
    main("startinguserdata.csv")




                      
            
        
