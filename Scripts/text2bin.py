"""
This is basic module to load database from text file. For test purposal only
Author: Pavel
    """
import pickle

#Import all the functions requied to manage db
from db import db_create
from db import db_add_entry
from db import db_form_entry

PATH = "./database.txt"
print("I: Attempting to open file: " + PATH)
FILE = open(PATH, 'r')
DATABASE = db_create()
CONTENT = FILE.read()
for entry_data in CONTENT.split("какаха"):#Спасибо, Маша
    params = entry_data.splitlines()[1::2]
    values = entry_data.splitlines()[2::2]
    entry = db_form_entry(params, values)
    db_add_entry(DATABASE, entry)
pickle.dump(DATABASE, open("db.pickle", 'wb'))
