import time
from os import system, name
from acctcreation import acctcreation

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

    accounts = acctcreation("bankdatabase.csv")
    gui(accounts)
    


def gui(database):
    print("welcome! What would you like to do:")
    a = True
    while(a):
        print("1. Log in")
        print("2. Make new account")
        print("3. Exit")
        selection = input("")

        #time.sleep(1)
        #clear()
        
        if(selection == "1"):
            a = False
            print("TODO line 39")
            #TODO make login stuff
            user = database.login()
            if not user:
                a = True
            else:        
                logged_in(database, user)
    
        elif(selection == "2"):
            print("Making a new account...")
            database.create_acct()
        elif(selection == "3"):
            a = False
            print("Saving data...")
            database.export()
            exit()

        else:
            print("Input not recognized, try again.")
            

    print("ending. delete this line 59")

#TODO finish this
def logged_in(database, user):
    #clear()
    print(f"Welcome {user}!")
    print("1. Deposite money")
    print("2. Withdraw money")
    valid = False
    selection = input("")
    while valid == False:
        if selection == 1:
            valid = True
            database.add_money(user)
        elif selection == 2:
            valid = True
            database.take_money(user)
        else:
            print("Select a valid response")

   



if __name__ == "__main__":
    main()
