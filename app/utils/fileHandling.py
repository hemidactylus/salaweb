'''
    pathHelper.py : path manipulation utilities
'''

import os

def pathLeadingPart(pth):
    h,t=os.path.split(pth)
    while(h!=''):
        h,t=os.path.split(h)
    return t

def getRole(dirName):
    '''
        looks in the absolute path dirName
        for a _ROLE specification
    '''
    roleFilename=os.path.join(dirName,'_ROLE')
    if os.path.isfile(roleFilename):
        return open(roleFilename).read().strip()
    else:
        return None
