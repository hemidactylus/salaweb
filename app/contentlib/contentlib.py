'''
    contentlib.py : utilities to load and operate on content descriptors
'''

import json
import os

def loadContents(dirName,fileName):
    '''
        loads content descriptors from a directory and returns the
        corresponding dictionary
    '''
    jsonName=os.path.join(dirName,fileName)
    print(jsonName)
    try:
        return json.load(open(jsonName))
    except:
        return {}
