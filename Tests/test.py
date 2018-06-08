import sys
# Adds higher directory to python modules path.
sys.path.append("../Scripts/")
#Import all the functions requied to manage db
from db import db_create
from db import db_add_entry
from db import db_form_entry

#Tests here
"""db = db_create()
params = {"artist"}
entry = db_form_entry(params,{"String"})
db_add_entry(db,entry)
db_add_entry(db,db_form_entry(params,{"String2"}))
db_add_entry(db,db_form_entry(params,{"String"}))
found = db_find_strict(db, {"artist":"String"})"""