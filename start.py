import time
from os import system, name
from acctcreation import acctcreation
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
    accounts = acctcreation("startinguserdata.csv")
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
            database.create_acct()
    
        elif(selection == "2"):
            a = False
            #TODO call make new user function
            print("Making a new account...")
        else:
            print("Input not recognized, try again.")
            

    print("ending")

if __name__ == "__main__":
    main()