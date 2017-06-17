#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="The name of the file you want to get the extension of.")
args = parser.parse_args()

def ext():
    file = args.file
    file = file.strip()
    file = file.split('.')
    del file[1:]
    file = ''.join(file)
    file = file.upper()
    ext = args.file
    ext = ext.strip()
    ext = ext.split('.')
    del ext[:-1]
    ext = ''.join(ext)
    ext = "." + ext
    ext = ext.upper()
    full = args.file
    full = ''.join(full)
    full = full.upper()
    if ('.' in full):
        print(file, "is a", ext, "file.")
    else:
        print(full, "is not a file.")

ext()
