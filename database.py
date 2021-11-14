class Catalog():

    
    def __init__(self, filePath):
        """ Initializes the catalog

        Args:
            filePath (string): path to file to be read
        """
        self.catalog = {}

        f = open(filePath, 'r')
        reader = f.readline()
        while(reader):
            listOfStuff = reader.strip().split(",")


            reader = f.readline()
        f.close()
    

    def get_balance(self, name):
        """ returns the user's balance
        
        Args:
            name: the user's username
        """
        return 0


    def add_user(self, user):
        """ 
        
        Args:
            user (user class): an instance of the user class
            
        """

        return