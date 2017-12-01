'''
    contentlib.py : utilities to load and operate on content descriptors
'''

from flask import (
    url_for,
)
import json
import os

def getRoles(user):
    return set() if not user.is_authenticated else user.roleSet()
def canSeeItem(user,item):
    return 'role' not in item or item['role'] in getRoles(user)
def resolveLinks(user,itemStructure):
    if 'endpoint' in itemStructure:
        itemStructure['href']=url_for(itemStructure['endpoint'],**itemStructure.get('kwargs',{}))
    if 'directory' in itemStructure:
        itemStructure['href']=url_for('ep_directory',relpath=itemStructure['directory'])
    if 'itemlist' in itemStructure:
        itemStructure['itemlist']=prepareItems(user,itemStructure['itemlist'])
    return itemStructure
def prepareItems(user,menuItems):
    '''
        this accepts the user and a list of items
    '''
    return [
        resolveLinks(user,mItem)
        for mItem in menuItems
        if canSeeItem(user,mItem)
    ]

def loadContents(user,dirName,fileName):
    '''
        loads content descriptors from a directory and returns the
        corresponding dictionary
    '''
    jsonName=os.path.join(dirName,fileName)
    try:
        return resolveLinks(user,json.load(open(jsonName)))
    except:
        print('Exception resolving "%s"' % jsonName)
        return {}
