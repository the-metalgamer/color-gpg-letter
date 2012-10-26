#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import with_statement

import argparse
import os.path
import sys

import common
import encrypt
import decrypt

parser = argparse.ArgumentParser()


parser.add_argument("source", help="The file to encrypt or decrypt (based on extension)", metavar="SOURCE", nargs="?", default=sys.stdin)

parser.add_argument("dest", help="The destination", metavar="DEST", nargs="?", default=sys.stdout)

group = parser.add_mutually_exclusive_group()

group.add_argument("-d", "--decrypt", action="store_true", help="Force decryption")
group.add_argument("-e", "--encrypt", action="store_true", help="Force encryption")

parser.add_argument("-c", "--colorfile", type=str, help="The color file to use, defaults to colors.json", metavar="FILE")
parser.add_argument("-s", "--pixelfactor", type=int, help="The factor to be used as pixelsize", metavar="N", default=1)

args = parser.parse_args()

if not args.colorfile:
    colorfile = None
else:
    colorfile = args.colorfile

colors = common.get_colors(colorfile)

if args.encrypt:
    doencrypt = True
elif args.decrypt:
    doencrypt = False
elif not args.encrypt and not args.decrypt:
    if os.path.splitext(args.source)[1] == ".asc":
        doencrypt = True
    elif os.path.splitext(args.source)[1] == ".png":
        doencrypt = False

if doencrypt:
    encrypt.encrypt(infile=args.source, outfile=args.dest, colors=colors, factor=args.pixelfactor)
else:
    decrypt.decrypt(infile=args.source, outfile=args.dest, colors=colors, factor=args.pixelfactor)
