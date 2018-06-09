# -*- coding: utf-8 -*-
"""
This is basic db module used to manage db in ram:
    Create, edit, compare and delete entries
"""
import pickle #To store db in FS and load it back

def db_load(path):
    """A function to load db
    Args:
        path - path to db file
    Returns:
        Database
    Author: Pavel
    """
    file = open(path, "rb")
    database = pickle.load(file)
    file.close()
    return database

def db_store(database, path):
    """A fucntion to store all db data with pickle
    Args:
        DATABASE - local database var
        path - path to db file
    Author: Pavel
    """
    file = open(path, "wb")
    pickle.dump(database, file)
    file.close()

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
    return unique_id

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

def db_set_entry_value(db, key, param, value):
    """ This function is used to edit an entry value.
    Args:
        db - database
        key - hash
        param - param to change
        value - new param value
    Author: Pavel
        """
    db[key][param] = value
    unique_id = hash(str(db[key][param]))
    db[unique_id] = db[key]
    del db[key]
    return unique_id

def db_get_keys(database):
    """This function returns all the keys avaible in DataBase
    This should be extremely helpfull in GUI
    Args:
        DB - database
    Returns:
        List of keys
    """
    all_keys = []
    for i in database:
        for j in database[i].keys():
            if j not in all_keys:
                all_keys.append(j)
    return all_keys

#def db_to_str_list(db):
#    """ Useless KOSTYL
#    TODO: Rewrite
#    Authors: Pavel, Andrew
#    """
#    trash = []
#    out = []
#    for element in db.values():
#        trash.append(tuple(element.values()))
#    for args in trash:
#        out.append('{0:<25} {1:>25} {2:>25} {3:>25}'.format(*args))
#    return out
