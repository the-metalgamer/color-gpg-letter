#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import with_statement

import sys
import StringIO

import Image


def swapdict(dictionary):
    '''
    Function to swap the values with the keys in a dict
    '''

    newdict = dict(zip(dictionary.values(), dictionary.keys()))

    return newdict


def splitlist(input, size):
    '''
    Function to split a list in lists of a certain size
    '''

    return map(None, *([iter(input)] * size))


def decrypt(infile, outfile, colors, factor=1):
    '''
    Function to decrypt a PNG to txt

    @param infile: The PNG to decrypt
    @param outfile: The file to save the output
    @param colors: The colors to use
    @param factor: The pixelsize used
    '''


    colors = swapdict(colors)

    if infile == sys.stdin:
        infile = StringIO.StringIO(sys.stdin.read())

    img = Image.open(infile)

    data = img.getdata()
    data = list(data)
    splitted_data = []

    for line in splitlist(data, img.size[0]):
        splitted_data.append(line)

    corrected_data = []
    for line in splitted_data[::factor]:
        chars = []
        for char in line[::factor]:
            chars.append(char)
        corrected_data.append(chars)

    if outfile != sys.stdout:
        outfile = open(outfile,'w')

    with outfile as f:
        for line in corrected_data:
            for color in line:
                    f.write(colors[color])
            f.write("\n")
