'''
    dbValues.py : initial values to write to DB
    upon creation of the database
'''

import env

from app.userspace.models import (
    User,
)

initialContents={
    'users': {
        'model': User,
        'values': [
            {
                'username': 'john',
                'fullname': 'John R',
                'email': 'someone@domain.com',
                'password': '123',
                'roles': '',
            }
        ],
    },
}
