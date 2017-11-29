'''
    dbschema.py : description of the database structure
'''

dbTablesDesc={
    'users': {
        'primary_key': [
            ('username', 'TEXT'),
        ],
        'columns': [
            ('fullname', 'TEXT'),
            ('passwordhash','TEXT'),
            ('email', 'TEXT'),
            ('roles', 'TEXT'),
        ],
    },
}
