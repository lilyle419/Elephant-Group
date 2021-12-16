def userChoice():
    end = ""
    while end != "end":
        # user has to enter the
        options = input("Would you like to make a deposit or withdraw?")
        if options == "withdraw":
            amount = float(input("How much?"))
            if(amount > database[user]):
                print("Insufficient funds")
            else:
                   database[user] = database[user] - amount
        else:
            if options == "deposit":
                 amount = float(input("How much?"))
                 database[user] = database[user] + amount
        print("Your current account balance is: $" + str(database[user]))
        end = input("Do you want to make another transaction? Yes or end")
    
userChoice()