#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import with_statement

import Image


def get_size(infile, factor):

    lines = (max(enumerate(open(infile, 'r')))[0] + 1) * factor
    columns = (len(max(open(infile, 'r'), key=len)) - 1) * factor
    return (columns, lines)


def encrypt(infile, outfile, colors, factor=1):

    size = get_size(infile, factor)

    img = Image.new("RGB", size, (255, 255, 255))

    data = []
    with open(infile) as f:
        for line in f:
            imageline = []
            for char in line.ljust(65, " "):

                if char != "\n":
                    imageline.append(colors[char])
                elif char == "\n":
                    data.append(imageline)

    extendeddata = []

    for line in data:
        charline = []
        for char in line:
            charline.append([char]*factor)
        extendeddata.append([charline]*factor)

    clean_data = []
    for i in extendeddata:
        for j in i:
            for k in j:
                for a in k:
                    clean_data.append(a)

    img.putdata(clean_data)

    img.save(outfile)
