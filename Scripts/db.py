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
    database = {}
    return database

def db_add_entry(database, value):
    """
    This function is supposed to add db entries
    Author: Pavel
    """
    unique_id = hash(str(value))
    database[unique_id] = value
    return unique_id

def db_delete_entry(database, index):
    """
    This function is supposed to add db entries
    Author: Pavel
    """
    del database[index]

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

def db_find_strict(database, params):
    """ This function lists all the entries that match the params
    Args:
        db - database, nothing to comment on :D
        params - dictionary of params and valuse like:
            { param1 : value1;
              param2 : value2... }
            }
    Attention! The entry will be returned only if ALL the params match their values
    Returns a dict of entries(dics) or an empty list
    Author: Pavel
    """
    found = {} #This list will store all the matching entries
    for current_entry in database:
        is_ok = 1
        for param in params:
            if database[current_entry][param] != params[param]:
                is_ok = 0
        if is_ok:
            found[current_entry] = database[current_entry]
    return found

def db_find_by_substr(database, key, substr):
    """Search for entries with key matching substr
    Author: Pavel"""
    found = []
    for current_entry in database:
        if substr in database[current_entry][key]:
            found.append(database[current_entry])
    return found

def db_list_greater_than(database, param, value):
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
    for current_entry in database:
        if int(database[current_entry][param]) > value:
            found.append(database[current_entry])
    return found

def db_list_lesser_than(database, param, value):
    """ This function lists all the entries with 'param' value is lesser
        than the given value
        Args:
            db - database, nothing to comment on :D
            value - int, to be compared
            param - param that should be compared against value
        Returns a list of entries(dics) or an empty list
        Author: Pavel
    """
    found = [] #This list will store all the matching entries
    for current_entry in database:
        if int(database[current_entry][param]) < value:
            found.append(database[current_entry])
    return found

def db_set_entry_value(database, key, param, value):
    """ This function is used to edit an entry value.
    Args:
        db - database
        key - hash
        param - param to change
        value - new param value
    Returns: new entry id
    Author: Pavel
    """
    database[key][param] = value
    unique_id = hash(str(database[key][param]))
    database[unique_id] = database[key]
    del database[key]
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

def db_mean(database, key):
    """Mean value for a key
    Args:
        database
        key - examined key (string)
    Returns:
        Mean value - signed integer
    """
    summa = 0
    amount = 0
    for value in database.values():
        summa += int(value[key])
        amount += 1
    return summa/amount

def db_keys_to_list(database, key):
    """List all the values for a key in a list
    Args:
        database
        key - text key (e. g. 'year' )
    Returns:
        list of values (strings in most cases)
    Author: Pavel
    """
    lst = []
    for value in database.values():
        lst.append(value[key])
    return lst

def db_max(database, key):
    """Maximum value for a key
    Args:
        database -satabase
        key - a key to examine
    Author: Pavel"""
    lst = db_keys_to_list(database, key)
    lst = [int(i) for i in lst]
    return max(lst)

def db_min(database, key):
    """Minimum value for a key
    Args:
        database -satabase
        key - a key to examine
    Author: Pavel"""
    lst = db_keys_to_list(database, key)
    lst = [int(i) for i in lst]
    return min(lst)

def db_most(database, key):
    """Find the most common element in a list
    Author: Pavel"""
    lst = db_keys_to_list(database, key)
    return max(set(lst), key=lst.count)

#Now for filters. DO NOT EDIT unless you're 100% it does not break filter
    
def gt(old_db, field, data):
    """Greater filter
    Author: Pavel"""
    new_db = db_create()
    items = db_list_greater_than(old_db, field, int(data))
    for i in items:
        db_add_entry(new_db, i)
    return new_db

def lt(old_db, field, data):
    """Lesser filter
    Author: Pavel"""
    new_db = db_create()
    items = db_list_lesser_than(old_db, field, int(data))
    for i in items:
        db_add_entry(new_db, i)
    return new_db

def eq(old_db, field, data):
    """Equality filter
    Author: Pavel"""
    new_db = db_create()
    items = db_find_strict(old_db, {field : data})
    for i in items:
        db_add_entry(new_db, old_db[i])
    return new_db

def inc(old_db, field, data):
    """Check if data is a substring of the given field
    Author: Pavel"""
    new_db = db_create()
    items = db_find_by_substr(old_db, field, data)
    for i in items:
        db_add_entry(new_db, i)
    return new_db