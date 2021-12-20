import hashlib
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
        """Allows users to create a sufficient bank account

            Side effects:
                adds a new account to the database
        
        """   
        created_account = False
        while (created_account is False):
            username = input("Enter your desired username:")
            pass1 = input("Enter your desired password:\nPassword must have a special character, a number, and a capital number:\n")
            
            if self.check_password(pass1) == True:


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
                    # integrate password.py related code here
                    password = Password()
                    salt = uuid.uuid4().hex
                    hashedpass = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
                    deposit = input("Please deposit any initial funds or put 0 if you so choose:")
                    self.userinfo[username] = (salt, hashedpass, float(deposit)) #key:username  tuple: salt, hashedpass, money
                    created_account = True
                    
                    
            elif self.check_password(pass1) == False:
                print("Intital password insufficent, activating password generator")
                password = Password()
                salt = uuid.uuid4().hex
                hashedpass = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
                deposit = input("Please deposit any initial funds or put 0 if you so choose:")
                self.userinfo[username] = (salt, hashedpass, float(deposit)) #key:username  tuple: salt, hashedpass, money
                created_account = True
 
            
            else:
                print("Passwords do not match. Please try again")
        


    def check_password(self, password):
        """Checks users password for necessary requirments

        Args:
            password(string): users desired password
        Returns:
            password_good(Boolean): True if password meets requirements
        """   
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

    def add_money(self, user, money): 
        """Withdraws money from users acocount

        Args:
            user(string): The user
            money(int): The amount they want to withdraw
        Side Effects: 
            Updates users money
        """   
        x = list(self.userinfo[user])
        x[2] = x[2] + money
        y = tuple(x)
        self.userinfo[user] = x

    def take_money(self, user, money):
        """Withdraws money from users acocount

        Args:
            user(string): The user
            money(int): The amount they want to withdraw
        Side Effects: 
            Updates users money
`       """

        x = list(self.userinfo[user])
        if(x[2]< money):
            print("You don't have enough funds. Exiting...")
            exit()

        x[2] = x[2] - money
        y = tuple(x)
        self.userinfo[user] = x


    def get_balance(self, user):
        """ returns the user's balance
        
        Args:
            user: the user's username
        """
        x = list(self.userinfo[user])
        return x[2]


    def add_user(self, user, password, money):
        """ adds a user to the catalog
        
        Args:
            user (string): an instance of the user class
            password (string): the user's inputted password
            money (float): money account starts with
        """

        salt = uuid.uuid4().hex
        hashedpass = hashlib.sha256(user[1].encode('utf-8') + salt.encode('utf-8')).hexdigest()

        x = (salt, hashedpass, money)
        self.userinfo[user] = x
        return

    def login(self):
        """ Prompts user for login info

        Returns (String): username if successful, empty string otherwise
        """
        good_login = False
        login_attempts = 0
        
        while (good_login is False):

            username = input("Enter your username:")
            if username in self.userinfo:

                password = input("Enter your password:")

                salt = self.userinfo[username][0]

                hashedinput = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

                if(hashedinput == self.userinfo[username][1]):

                    print("Success! Logging you in.")
                    return username

                else:
                    print ("Incorrect username or password please try again.")
                    login_attempts += 1
                
            else:
                print ("Incorrect username or password please try again.")
                login_attempts += 1
            if login_attempts >= 3:
                print ("Too many failed attempts. Try again later.")
                return ""


        return ""


    def export(self):
        """Exports dictionary of updated info to the database

        Side Effects:
            updates database
        """
        print("this function will export out current dictionary to bankdatabase.csv")

        f = open("bankdatabase.csv", 'w')

        for key in self.userinfo.keys():
            a = self.userinfo[key]
            line = f"{key},{a[0]},{a[1]},{a[2]}\n"
            f.write(line)
        
        f.close()
        print("export finished!")



def lettersgen():
    """Helper function for adding characters to the password

        Returns:
            letterlist(string): adds letters

"""
    lettersList = []
    userLetters = int(input("How many letters?"))
    for i in range(userLetters):
        letPW = random.choice(letters)
        lettersList.append(letPW)
    return lettersList

def numbersgen():
    """Helper function for adding numbers to the password

        Returns:
            numlist(string): adds numbers

"""
    numList = []
    userNum = int(input("How many numbers?"))
    for i in range(userNum):
        numPW = random.choice(numbers)
        numList.append(numPW)
    return numList

def symGen():
    """Helper function for adding symbols to the passwords

        Returns:
            symlist(string): adds symbols

"""
    symList = []
    userSym = int(input("How many special characters?"))
    for i in range(userSym):
        symPW = random.choice(sym)
        symList.append(symPW)
    return symList

def Password():
    """Generates a password using helper functions

        Returns:
            finalpass(string): The generated password

"""
    
    print("Welcome! Creating generated password:")
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
    return finalpass

