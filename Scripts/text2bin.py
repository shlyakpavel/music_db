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
file = open(PATH, 'r')
database = db_create()
content = file.read()
for entry_data in content.split("какаха"):#Спасибо, Маша
    params = entry_data.splitlines()[1::2]
    values = entry_data.splitlines()[2::2]
    entry = db_form_entry(params, values)
    db_add_entry(database, entry)
pickle.dump(database, open("db.pickle", 'wb'))