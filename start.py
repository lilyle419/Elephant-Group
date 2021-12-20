import time
from os import system, name
from acctcreation import acctcreation

def clear():
    """clears user's terminal
    https://stackoverflow.com/questions/54943464/how-to-clear-a-screen-in-python/54943542#54943542
    techdoodle

    The clear function was used here to have our output look cleaner
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    print("Starting up...")
    time.sleep(1)
    clear()

    accounts = acctcreation("bankdatabase.csv")
    gui(accounts)
    


def gui(database):
    """The main text based user interface

    Args:
        database (acctcreation): the current bank database.
    
    """

    print("Welcome! What would you like to do:")
    a = True
    while(a):
        print("1. Log in")
        print("2. Make new account")
        print("3. Exit")
        selection = input("")

        time.sleep(1)
        clear()
        
        if(selection == "1"):
            a = False
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

    print("Have a nice day!")            

    


def logged_in(database, user):
    """ The text based user interface for when the user is logged in

    Args:
        database(acctcreation): the current bank database.
        user(String): the user's username
    
    
    """
    clear()
    print(f"Welcome {user}!")
    print("1. Deposite money")
    print("2. Withdraw money")
    valid = False
    selection = input("")
    while valid == False:
        if selection == "1":
            clear()
            valid = True
            print(f"You currently have ${database.get_balance(user)}")
            money = input("How much are you depositing: $")
            money = int(money)

            database.add_money(user, money)
            print("Saving data...")
            time.sleep(1)
            database.export()
            print("Thank you for working with Elephant Banking!")
            exit()
        elif selection == "2":
            clear()
            valid = True
            print(f"You currently have ${database.get_balance(user)}")
            money = input("How much are you withdrawing: $")
            money = int(money)
            database.take_money(user, money)

            print("Saving data...")
            time.sleep(1)
            database.export()
            print("Thank you for working with Elephant Banking!")
            exit()

        else:
            print("Select a valid response")
            selection = input("")

   

if __name__ == "__main__":
    main()
