import time
from os import system, name
from acctcreation import acctcreation
import random
import string
# import password

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    print("starting up...")
  #  time.sleep(1)
  #  clear()
  #  TODO insert importing data from csv file
    accounts = acctcreation("bankdatabase.csv")
    gui(accounts)
    


def gui(database):
    print("welcome! What would you like to do:")
    a = True
    while(a):
        print("1. Log in")
        print("2. Make new account")
        selection = input("")

        #time.sleep(1)
        #clear()
        
        if(selection == "1"):
            a = False
            print("TODO line 39")
            #TODO make login stuff
            #create code for looking at user's current balance
    
        elif(selection == "2"):
            a = False
            print("Making a new account...")
            database.create_acct()
        else:
            print("Input not recognized, try again.")
            

    print("ending")
sym = "!@$%^&*()-+]#"
letters = string.ascii_letters
numbers = string.digits
def lettersgen():
    lettersList = []
    userLetters = int(input("How many letters?"))
    for i in range(userLetters):
        letPW = random.choice(letters)
        lettersList.append(letPW)
    return lettersList
def numbersgen():
    numList = []
    userNum = int(input("How many numbers?"))
    for i in range(userNum):
        numPW = random.choice(numbers)
        numList.append(numPW)
    return numList
def symGen():
    symList = []
    userSym = int(input("How many special characters?"))
    for i in range(userSym):
        symPW = random.choice(sym)
        symList.append(symPW)
    return symList
def Password():
    userInput = ""
    while userInput != "done":
        userInput = input("Welcome! Create password (yes or done):")
        if userInput == "done":
            break
        lettersPass= lettersgen()
        numPass = numbersgen()
        symPass = symGen()
        password = []
        password.extend(lettersPass)
        password.extend(numPass)
        password.extend(symPass)
        random.shuffle(password)
        finalpass = ''.join(str(char)for char in password)
        print(finalpass)
        
Password()

if __name__ == "__main__":
    main()
