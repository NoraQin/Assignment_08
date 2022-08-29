#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# qinlaura, 2022-Aug-28, completed code
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    '''Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        None

    '''
    # -- Constructor -- #
    def __init__(self, id: int, title: str, artist: str):
        # -- Attributes -- #
        self.__cd_id = id
        self.__cd_title = title
        self.__cd_artist = artist
    
    # -- Properties -- #
    @property
    def cd_id(self):
        '''Getter for cd_id.'''
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        '''Setting for cd_id. Raises an exception if value passed in is not numeric.'''
        if type(value) != int:
            raise Exception('ID must be numeric.')
        else:
            self.__cd_id = value
    
    @property
    def cd_title(self):
        '''Getter for cd_title.'''
        return self.__cd_title.title()
    @cd_title.setter
    def cd_title(self, value):
        '''Setter for cd_title.'''
        self.__cd_title = value
    
    @property
    def cd_artist(self):
        '''Getter for cd_artist.'''
        return self.__cd_artist.title()
    @cd_artist.setter
    def cd_artist(self, value):
        '''Setter for cd_artist.'''
        self.__cd_artist = value

# -- PROCESSING -- #
class FileIO:
    '''Processes data to and from file:

    properties:
        None

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    '''
    # -- Methods -- #
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        '''Save the inventory data into file.

        Args: 
            file_name (string): name of file to save data to
            lst_Inventory (list of CD objects): the CD inventory data being stored in memory
        
        Returns: 
            None
        '''
        obj_file = open(file_name, 'w')
        for cd in lst_Inventory:
            line = ','.join([str(cd.cd_id), cd.cd_title, cd.cd_artist])
            obj_file.write(line + '\n')
        obj_file.close()
    
    @staticmethod
    def load_inventory(file_name):
        '''Load inventory data in file into memory.

        Args: 
            file_name (string): name of file to load data from
        
        Returns: 
            lst_Inventory (list of CD objects): the CD inventory data being stored in memory
        '''
        try:
            lst_Inventory = []
            obj_file = open(file_name, 'r')
            for line in obj_file:
                l = line.strip().split(',')
                cd = CD(int(l[0]), l[1], l[2])
                lst_Inventory.append(cd)
            return lst_Inventory
        except FileNotFoundError as e:
            print('\nFile cannot be found.')
            return []
        except Exception as e:
            print('\nThere was a general error. Here are the details: ')
            print(type(e), e, e.__doc__, sep = '\n')
            return []

# -- PRESENTATION (Input/Output) -- #
class IO:
    '''Processes data to and from file:

    properties:
        None

    methods:
        print_menu(): -> None
        get_menu_choice(): -> str
        display_data(lst_Inventory): -> None
        get_cd(): -> a CD object
        get_load_yes_no(): -> str

    '''
    # -- Methods -- #
    @staticmethod
    def display_menu():
        '''Displays menu options.

        Args: 
            None
        
        Returns: 
            None
        '''
        print('\nMenu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def get_menu_choice():
        '''Get user's choice.

        Args: 
            None
        
        Returns: 
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        '''
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()
        return choice
    
    @staticmethod
    def display_data(lst_Inventory):
        '''Show what's currently in the data in memory.

        Args: 
            lst_Inventory (list of CD objects): the CD inventory data being stored in memory
        
        Returns: 
            None
        '''
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in lst_Inventory:
            print('{}\t{} (by:{})'.format(str(cd.cd_id), cd.cd_title, cd.cd_artist))
        print('======================================')

    @staticmethod
    def get_cd():
        '''Ask user to enter information of a new CD and return a new CD object

        Args: 
            None
        
        Returns: 
            cd (a CD object): a new CD object populated with user input
        '''
        try:
            id = int(input('Enter ID: '))
            title = input('Enter title: ')
            artist = input('Enter artist: ')
            cd = CD(id, title, artist)
            return cd
        except ValueError as e:
            print('\nID must be an integer.')
            return None
        except Exception as e:
            print('\nThere was a general error. Here are the details: ')
            print(type(e), e, e.__doc__, sep = '\n')
            return None
    
    @staticmethod
    def get_load_yes_no():
        '''Print out a warning, and ask user if they want to proceed to load data from file or not

        Args: 
            None
        
        Returns: 
            choice (str): whether the user wants to proceed with loading data, 'y' or 'n'
        '''
        choice = input('Loading from file will erase all unsaved data. Are you sure? [y/n]: ')
        return choice

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

while True:
    # Display menu to user
    IO.display_menu()

    # capture user's selection
    menu_choice = IO.get_menu_choice()

    # show user current inventory
    if menu_choice == 'i':
        IO.display_data(lstOfCDObjects)

    # let user add data to the inventory
    elif menu_choice == 'a':
        new_cd_obj = IO.get_cd()
        if new_cd_obj is not None:
            lstOfCDObjects.append(new_cd_obj)

    # let user save inventory to file
    elif menu_choice == 's':
        FileIO.save_inventory(strFileName, lstOfCDObjects)

    # let user load inventory from file
    elif menu_choice == 'l':
        load_yes_no = IO.get_load_yes_no()
        if load_yes_no == 'y':
            lstOfCDObjects = FileIO.load_inventory(strFileName)

    # let user exit program
    elif menu_choice == 'x':
        break

    # handle invalid menu choice
    else:
        print('Invalid choice, please select again.')