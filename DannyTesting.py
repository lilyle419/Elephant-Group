import hashlib
import base64
import uuid
from argparse import ArgumentParser
import sys

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
