'''
    dbgenerate.py : creation of the database from the schema and some starting values
'''

import sys
import os

import env

from app.Sqlite.sqliteEngine import (
    dbOpenDatabase,
    dbCreateTable,
    dbAddRecordToTable,
)

from config import dbFullName

from app.userspace.dbschema import dbTablesDesc
from app.userspace.models import User
from app.userspace.dbValues import initialContents

if __name__=='__main__':
    if '-f' in sys.argv[1:] or not os.path.isfile(dbFullName):
        if os.path.isfile(dbFullName):
            print(' * Deleting old DB')
            os.remove(dbFullName)
        #
        print(' * Creating DB')
        db=dbOpenDatabase(dbFullName)
        print(' * Creating tables')
        for tName, tContents in dbTablesDesc.items():
            print('     * %s' % tName)
            dbCreateTable(db, tName, tContents)
        print(' * Done.')
        # insertions
        for table,tcontents in initialContents.items():
            print(' * Inserting into table "%s"' % table)
            for item in tcontents['values']:
                model=tcontents['model'](**item)
                dbAddRecordToTable(db,table,model.asDict(),dbTablesDesc=dbTablesDesc)
                print('      # %s' % model)
        db.commit()
    else:
        print('File "%s" exists' % dbFullName)
