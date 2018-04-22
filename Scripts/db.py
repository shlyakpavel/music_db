# -*- coding: utf-8 -*-
"""
This is basic db module used to manage db in ram:
    Create, edit, compare and delete entries
"""

def db_create():
    """
    This function is used to create empty db var (dict of dicts)
    Author: Pavel
    """
    db = {}
    return db

def db_add_entry(db, value):
    """
    This function is supposed to add db entries
    Author: Pavel
    """
    unique_id = hash(str(value))
    db[unique_id] = value
    return 0

def db_form_entry(params, values):
    """ This function forms an entry
    Args:
        params - parameters used in db
        values - values of these parameters
    Author: Pavel
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
    Author: Pavel
    """
    found = [] #This list will store all the matching entries
    for current_entry in db:
        is_ok = 1
        for param in params:
            if db[current_entry][param] != params[param]:
                is_ok = 0
        if is_ok:
            found.append(db[current_entry])
    return found

def db_list_greater_than(db, param, value):
    """ This function lists all the entries with 'param' value is greater
        than the given value
        Args:
            db - database, nothing to comment on :D
            value - int, to be compared
            param - param that should be compared against value
        Returns a list of entries(dics) or an empty list
        Author: Andrey
    """
    found = [] #This list will store all the matching entries
    for current_entry in db:
        if int(db[current_entry][param]) >= value:
            found.append(db[current_entry])
    return found

def db_set_entry_value(entry, param, value):
    """ This function is used to edit an entry value.
    Args:
        entry - database entry
        param
    Author: Pavel
        """
    entry[param] = value
"""db = db_create()
params = {"artist"}
entry = db_form_entry(params,{"String"})
db_add_entry(db,entry)
db_add_entry(db,db_form_entry(params,{"String2"}))
db_add_entry(db,db_form_entry(params,{"String"}))
found = db_find_strict(db, {"artist":"String"})"""