#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import with_statement

import Image


def swapdict(dictionary):

    newdict = dict(zip(dictionary.values(), dictionary.keys()))

    return newdict


def splitlist(input, size):
    return map(None, *([iter(input)] * size))


def decrypt(infile, outfile, colors, factor=1):

    colors = swapdict(colors)

    img = Image.open(infile)
    #img = img.resize((img.size[0] / factor, img.size[1] / factor), Image.NEAREST)

    data = img.getdata()
    data = list(data)
    splitted_data = []

    for line in splitlist(data, 64 * factor):
        splitted_data.append(line)

    corrected_data = []
    for line in splitted_data[::factor]:
        chars = []
        for char in line[::factor]:
            chars.append(char)
        corrected_data.append(chars)

    with open(outfile, 'w') as f:
        for line in corrected_data:
            for color in line:
                    f.write(colors[color])
            f.write("\n")
