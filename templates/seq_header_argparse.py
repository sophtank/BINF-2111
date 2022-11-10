#!/bin/usr/env python3

import argparse

parser = argparse.ArgumentParser()
required = parser.add_argument_group("Required Arguments")
required.add_argument('-i','--input', type=str, help = 'path to intended input file')
#output line is commented out because it can be optional.
# required.add_argument('-o', '--output', type=str, help='path to intended output file')
args = parser.parse_args()
file_in = open(args.input)
lines = file_in.readlines()

header = []
seq = []

for line in lines:
    line = line.strip()

    if line[0] == '>':
        header.append(line)
    if line[0] != '>':
        seq.append(line)
