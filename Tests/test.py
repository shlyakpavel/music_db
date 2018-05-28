import sys
# Adds higher directory to python modules path.
sys.path.append("../Scripts/")
#Import all the functions requied to manage db
from db import db_create
from db import db_add_entry
from db import db_form_entry

#Tests here