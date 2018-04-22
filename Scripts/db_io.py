"""
This is basic I/O module used to manage i/o operations:
    Load and save database
    TODO: not to forget failsave mode
    """
#Import all the functions requied to manage db
from db import db_create
from db import db_add_entry
from db import db_form_entry
from db import db_set_entry_value
    
class IO:
    """docstring"""
 
    def __init__(self):
        """Constructor"""
        pass
    
    path = "./database.txt"
    file = None
    
    def setpath(self, path_str):
        self.path=path_str
        
    def load(self, file_path = path):
        """Function to load database from file
        Args:
            file_path - not requied if already set
        Author: Pavel"""
        #Read only (for the case we don't need output operations)
        file = open('text.txt', 'w+')
        db = db_create()
        return db
    
    def save(self, db):
        
        return 0