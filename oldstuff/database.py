import hashlib
import base64
import uuid
from argparse import ArgumentParser
import sys

class Catalog():
    
    def __init__(self, filePath):
        """ Initializes the catalog

        Args:
            filePath (string): path to file to be read
        """
        self.catalog = {}

        f = open(filePath, 'r')
        reader = f.readline()
        while(reader):
            listOfStuff = reader.strip().split(",")
            print(listOfStuff)

            reader = f.readline()
        f.close()
    

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


#_____________________testing stuff underhere_______________


def test_stuff():

    password = "Thisismypass123"
    salt = uuid.uuid4().hex

    
    hashed_pass = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

    print(f"password is:{password}, salt is:{salt}")
    print(f"hashed it is:{hashed_pass}")

    print(f"\nnow lets try again with a different user that has the same password\n")
    salt2 = uuid.uuid4().hex

    hashed_pass2 = hashlib.sha256(password.encode('utf-8') + salt2.encode('utf-8')).hexdigest()
    print(f"password is:{password}, salt2 is:{salt2}")
    print(f"hashed it is:{hashed_pass2}")

def check_password():

    return




#_______________


def main():
    test_stuff()
   
   


if __name__ == "__main__":
    main()
