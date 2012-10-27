#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        print("No json module found.")
        print("Exiting")
        exit(1)


standard_colors = {
    " ": (255,255,255),
    "A": (0,0,0),
    "B": (255,0,0),
    "C": (0,255,0),
    "D": (0,0,255),
    "E": (255,255,0),
    "F": (255,0,255),
    "G": (0,255,255),
    "H": (127,0,0),
    "I": (0,127,0),
    "J": (0,0,127),
    "K": (127,127,0),
    "L": (127,0,127),
    "M": (0,127,127),
    "N": (127,127,127),
    "O": (63,0,0),
    "P": (0,63,0),
    "Q": (0,0,63),
    "R": (63,63,0),
    "S": (63,0,63),
    "T": (0,63,63),
    "U": (63,63,63),
    "V": (190,0,0),
    "W": (0,190,0),
    "X": (0,0,190),
    "Y": (190,190,0),
    "Z": (190,0,190),
    "a": (0,190,190),
    "b": (190,190,190),
    "c": (255,63,0),
    "d": (255,0,63),
    "e": (255,63,63),
    "f": (63,255,0),
    "g": (0,255,63),
    "h": (63,255,63),
    "i": (63,0,255),
    "j": (0,63,255),
    "k": (63,63,255),
    "l": (255,127,0),
    "m": (255,0,127),
    "n": (255,127,127),
    "o": (127,255,0),
    "p": (0,255,127),
    "q": (127,255,127),
    "r": (127,0,255),
    "s": (0,127,255),
    "t": (127,127,255),
    "u": (255,190,0),
    "v": (255,0,190),
    "w": (255,190,190),
    "x": (190,255,0),
    "y": (0,255,190),
    "z": (190,255,190),
    "0": (190,0,255),
    "1": (0,190,255),
    "2": (190,190,255),
    "3": (127,190,255),
    "4": (190,255,127),
    "5": (255,127,190),
    "6": (63,127,190),
    "7": (127,190,63),
    "8": (190,63,127),
    "9": (63,127,255),
    "+": (127,255,63),
    "/": (255,63,127),
    "-": (63,190,190),
    ":": (190,190,63),
    ".": (190,63,190),
    "(": (63,127,127),
    ")": (127,127,63),
    "=": (127,63,127)
}

def tuplify(dictionary):
    '''
    Function to change the values of a list to a tuple
    '''

    for key in iter(dictionary):
        dictionary[key] = tuple(dictionary[key])


def get_colors(colorfile=None):
    '''
    Function to load the colors from a json file
    '''
    if colorfile is not None:
        colors = json.load(open(colorfile))
        tuplify(colors)
    else:
        colors = standard_colors


    return colors
