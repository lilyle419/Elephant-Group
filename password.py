# import random and string module
import random
import string
sym = "!@$%^&*()-+]#"
letters = string.ascii_letters
numbers = string.digits
# define functions
def lettersgen():
    lettersList = []
    userLetters = int(input("How many letters?"))
    for i in range(userLetters):
        # have the program choose random letters
        letPW = random.choice(letters)
        # use append to add the letters to the list 
        lettersList.append(letPW)
    return lettersList
def numbersgen():
    numList = []
    userNum = int(input("How many numbers?"))
    for i in range(userNum):
        # have the program choose random numbers
        numPW = random.choice(numbers)
        # use append to add the numbers to the list
        numList.append(numPW)
    return numList
def symGen():
    symList = []
    userSym = int(input("How many special characters?"))
    for i in range(userSym):
        # have the program choose random symbols from the string of symbols I provided in line 5
        symPW = random.choice(sym)
        # use append to add the symbols to the list
        symList.append(symPW)
    return symList
def Password():
    userInput = ""
    # create a while loop so the program runs until the user tells it to stop
    while userInput != "done":
        # welcome the user and prompt them to create a password
        userInput = input("Welcome! Create password (yes or done):")
        if userInput == "done":
            break
        lettersPass= lettersgen()
        numPass = numbersgen()
        symPass = symGen()
        password = []
        # use the extend function to combine the data 
        password.extend(lettersPass)
        password.extend(numPass)
        password.extend(symPass)
        # use the shuffle function to mix up all the random characters
        random.shuffle(password)
        # turn list back into a string
        # use join function to add all the items into a string
        finalpass = ''.join(str(char)for char in password)
        print(finalpass)
        
Password()

