import hashlib
import uuid


def test_stuff():

    password = "Thisismypass123!"
    salt = uuid.uuid4().hex
    potato = hashlib.sha256(password.encode('utf-8')).hexdigest()


    print()
    print()
    print(f"password is: |{password}|")
    print(f"hashed it is: |{potato}|")
    print()
    print()
    
    hashed_pass = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

    print(f"password is: |{password}|, salt is: |{salt}|")
    print(f"hashed it is: |{hashed_pass}|")

    print(f"\nnow lets try again with a different user that has the same password\n")
    salt2 = uuid.uuid4().hex

    hashed_pass2 = hashlib.sha256(password.encode('utf-8') + salt2.encode('utf-8')).hexdigest()
    print(f"password is: |{password}|, salt2 is: |{salt2}|")
    print(f"hashed it is: |{hashed_pass2}|")


def main():
    i = 0
    password = ["Realteal123", "Plaintivevole123", "Tawdrygnu123", "Seriousruffs123","Muddledbass123"]
    while(i < 5):
        salt = uuid.uuid4().hex
        password[i] = hashlib.sha256(password[i].encode('utf-8') + salt.encode('utf-8')).hexdigest()
        print(f"{salt},{password[i]}")

        i+=1
    exit()
    test_stuff()
   
   
if __name__ == "__main__":
    main()
