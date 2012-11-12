#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import with_statement

import sys

import Image


def get_size(infile, factor):
    '''
    Function to get lines an columns of a file
    '''

    if infile == sys.stdin:
        lines = (max(enumerate(infile))[0] + 1) * factor
    else:
        lines = (max(enumerate(open(infile, 'r')))[0] + 1) * factor
    columns = 64 * factor
    return (columns, lines)


def encrypt(infile, outfile, colors, factor=1):
    '''
    Function to encrypt a base64 encoded file to PNG

    @param infile: The file to encrypt
    @param outfile: The file to save to
    @param colors: The colors to use
    @param factor: The factor the size per pixel gets multiplied
    '''

    size = get_size(infile, factor)

    img = Image.new("RGB", size, (255, 255, 255))

    if infile != sys.stdin:
        infile = open(infile)

    data = []
    with infile as f:
        for line in f:
            imageline = []
            for char in line.ljust(65, " "):
                if char != "\n":
                    imageline.extend(([colors[char]] * factor))
                else:
                    data.extend([imageline] * factor)

    clean_data = []
    for i in data:
        clean_data.extend(i)

    img.putdata(clean_data)

    img.save(outfile, "PNG")
