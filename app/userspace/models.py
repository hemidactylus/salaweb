'''
    models.py : classes to interface with DB objects and the like
'''

import hashlib

class dictableObject():

    def asDict(self):
        return {k: getattr(self,k) for k in self.namedFields}

    def consumeKWargs(self, **kwargs):
        '''
            eats up and sets all kwargs appearing in the namedFields,
            returning the remaining ones for specialised handling
        '''
        _kwargs={k:v for k,v in kwargs.items()}
        delFields=[]
        for k,v in _kwargs.items():
            if k in self.namedFields:
                setattr(self,k,v)
                delFields.append(k)
        for df in delFields:
            del _kwargs[df]
        return _kwargs

class User(dictableObject):

    namedFields=['username','fullname','passwordhash', 'email', 'roles']

    def __init__(self,**kwargs):
        '''
            username, id, passwordhash
        '''
        _kwargs=self.consumeKWargs(**kwargs)
        if 'password' in _kwargs:
            self.passwordhash=self._hashString(_kwargs['password'])
            del _kwargs['password']
        if _kwargs:
            raise ValueError('Unknown argument(s): %s' % ', '.join(_kwargs.keys()))

    def roleSet(self):
        return set(self.roles.split(','))

    def hasRole(self,rolename):
        return rolename in self.roleSet()

    @staticmethod
    def _hashString(message):
        return hashlib.sha256(message.encode()).hexdigest()

    def checkPassword(self,stringToCheck):
        return self._hashString(stringToCheck) == self.passwordhash

    @property
    def is_authenticated(self):
        # True unless the object represents a user that should not be allowed to authenticate for some reason
        return True

    @property
    def is_active(self):
        # True for users unless they are inactive, for example because they have been banned
        return True

    @property
    def is_anonymous(self):
        # True only for fake users that are not supposed to log in to the system
        return False

    def get_id(self):
        # unique identifier for the user, in unicode format
        return str(self.username)  # python 3

    def __repr__(self):
        return '<User "%s" (%s)>' % (self.username, self.fullname)
