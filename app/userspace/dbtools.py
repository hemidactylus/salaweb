'''
    dbtools.py
'''

from app.userspace.models import (
    User,
)
from app.Sqlite.sqliteEngine import (
    dbRetrieveRecordByKey,
    dbOpenDatabase as _se_dbOpenDatabase,
)
from app.userspace.dbschema import dbTablesDesc as tdesc

def dbGetUser(db,username):
    userDict = dbRetrieveRecordByKey(db, 'users', {'username':username}, dbTablesDesc=tdesc)
    return User(**userDict) if userDict else None

def dbOpenDatabase(fn):
    return _se_dbOpenDatabase(fn,dbTablesDesc=tdesc)
