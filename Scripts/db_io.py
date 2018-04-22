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
    status = "NA"
        
    def load(self, file_path = None):
        """Function to load database from file
        Args:
            file_path - not requied if already set
        Author: Pavel"""
        if (file_path == None):
            file_path = self.path
        else:
            self.path = file_path
        #Read only (for the case we don't need output operations)
        print("I: Attempting to open file: " + file_path)
        self.file = open(file_path, 'r+')
        db = db_create()
        content = self.file.read()
        for entry_data in content.split("какаха"):#Спасибо, Маша
            params = entry_data.splitlines()[1::2];
            values = entry_data.splitlines()[2::2];
            entry = db_form_entry(params, values)
            db_add_entry(db, entry)
        self.status = "open"
        return db
    
    def save(self, db):
        
        return 0