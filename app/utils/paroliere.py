'''
    paroliere.py : functions to deal with the "Paroliere" game.
'''

import os
from random import shuffle, randint

basePath=os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
srcFile='letters.dat'

def loadDice():
    '''
        returns a list of dice, each as a list of one-char strings (the faces)
    '''
    return [
        list(line.strip())
        for line in open(os.path.join(basePath,srcFile)).readlines()
        if line.strip() != ''
    ]

def deal():
    d=loadDice()
    shuffle(d)
    return [
        die[randint(0,5)]
        for die in d
    ]
