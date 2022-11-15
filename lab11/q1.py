#!/usr/bin/env python3

#use argparse to load in CoV_furin_seq.faa
import argparse , re

parser = argparse.ArgumentParser()
required = parser.add_argument_group("Required Arguments")
required.add_argument('-i','--input', type=str, help = 'path to intended input file')
required.add_argument('-o', '--output', type=str, help='path to intended output file')
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

#function to do all that q1 asks for
def analysis(seq,header):
    i = 0
    for i in range (0,len(seq)):
        #print the length
        print("Length of " + str(header[i]) + " is " + str(len(seq[i])))
        #print wether the sequence started with M
        if re.search("^M", str(seq[i])):
            print("True")
        else:
            print("False")
        serine = round(( seq[i].count('S') / len(seq[i]) ) * 100,2)
        print("This sequence is " + str(serine) + "% serine.")
    #print the total sequence number
    print("There are " + str(len(seq)) + " sequences in the file.")

#opens the output file, outputs all sequences with the furin cleavage site (RSVAS)
with open(args.output, 'w') as reader:
    i= 0 
    for i in range(0,len(seq)):
        if re.search("RSVAS", seq[i]):
            reader.write(header[i] + "\n" + seq[i] + "\n")


analysis(seq,header)
