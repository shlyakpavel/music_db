# -*- coding: utf-8 -*-

def db_create():
    """
    This function is used to create empty db var (dict of dicts)
    """
    db = {}
    return db

def db_add_entry(db, value):
    """
    This function is supposed to add db entries
    """
    unique_id = hash(str(value))
    db[unique_id] = value
    return 0

def db_form_entry(params, values):
    """ This function forms an entry
    Args:
        params - parameters used in db
        values - values of these parameters
        !!!  params and values are collections only
    Author: Unknown
    """
    entry = zip(params, values)
    entry = dict(entry)
    return entry

def db_find_strict(db, params):
    """ This function lists all the entries that match the params
    Args:
        db - database, nothing to comment on :D
        params - dictionary of params and valuse like:
            { param1 : value1;
              param2 : value2... }
            }
    Attention! The entry will be returned only if ALL the params match their values
    Returns a list of entries(dics) or an empty list
    """
    found = [] #This list will store all the matching entries
    for current_entry in db:
        is_ok = 1;
        for param in params:
            if db[current_entry][param] != params[param]:
                is_ok = 0
        if is_ok:
            found.append(db[current_entry])
    return found;
        
    

def db_set_entry_value(entry, param, value):
    """ This function is used to edit an entry value.
    Args:
        entry - database entry
        param
        """
    entry[param] = value
def db_find_nonstrict_afterdate(db,year):
    """ This function lists all the entries starting from imported year
        year - int
    
    """
    found = [] #This list will store all the matching entries
    for current_entry in db:
        is_ok = 0;
        if int(db[current_entry]["year"]) >= year:
            is_ok = 1
        if is_ok:
            found.append(db[current_entry])
    return found;
        

db = db_create()
params = ["artist","year"];
entry = db_form_entry(params,{"String"})

db_add_entry(db,db_form_entry(params,["String","1985"]))
db_add_entry(db,db_form_entry(params,["String2","1974"]))
db_add_entry(db,db_form_entry(params,["String2","11"]))
found = db_find_strict(db, {"artist":"String","year":"1985"})
found2 = db_find_nonstrict_afterdate(db,1980)
