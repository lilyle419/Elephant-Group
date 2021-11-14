import sys
from argparse import ArgumentParser


class Login:

    
    
    def __init__(self, filepath):
       
        self.userinfo = {}
        
        with open(filepath, 'r', encoding = "utf-8") as new_file:
            for line in new_file:
                user = line.strip().split(",")
                self.userinfo[user[0]] = (user[1], float(user[2])) #key:username  tuple: password, money in account
    
    
    
    def login_attempt(self):
        
        good_login = 0
        
        while (good_login > 0):
            
            username = input("Enter your username:")

            if username in self.userinfo.keys():
                
                password = input("Enter your password:")

                if password == self.userinfo[username]:
                    good_login+=1
                    print("Login succesful")
                    #some code to allow them to access their specific account would come after"
            else:
                print ("Incorrect username or password")



def main(filename):
    print("hello")
    user_data = Login(filename)
    Login(user_data)

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filename: a path to a CSV file containing aardvark stats

    
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="path to CSV file containing aardvark stats")
  
    return parser.parse_args(arglist)



if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
            
                      
            
        
