#!/usr/bin/env python3

import argparse
#creating an argument parser and a group of required arguments
parser = argparse.ArgumentParser()
required = parser.add_argument_group("Required Arguments")
#adding required arguments to the group
required.add_argument('-i', '--input', type=str, help='path to file', required = True)

#making an argument parser
args = parser.parse_args()

#opening the file
file_in = open(args.input)

#creating list of lines
lines = file_in.readlines()

#creating empty lists for headers and sequences
header = []
seq = []

for line in lines:
        line = line.rstrip()

        if line[0] == '>':
            header.append(line)
        
        if line[0] != '>':
            seq.append(line)
print(header)
print(seq)

def aa_function(seq,header):

    #declaring a and i as zero for later functions
    i = 0


    for i in range(0,len(seq)):
                mcount = round(( seq[i].count('M') / len(seq[i]) ) * 100,2)
                lcount = round(( seq[i].count('L') / len(seq[i]) ) * 100,2)
                rcount = round(( seq[i].count('R') / len(seq[i]) ) * 100,2)
                ycount = round(( seq[i].count('Y') / len(seq[i]) ) * 100,2)
                print("Sequence " + header[i] + " has length " + str((len(seq[i]))))
                print("It is " + str(mcount) + "% Methionine, " + str(lcount) + "% Leucine, " + str(rcount) + "% Arginine, and " + str(ycount) + "% Tyrosine.") 

#function to count sequences starting with methionine        
def mcount(seq):
    count = 0
    for i in range(0,len(seq)):
        if seq[i].startswith("M"):
            count += 1
    print(str(count))
    return count
    
#function to count the amount of sequences
def seqcount(header):
    count = 0
    for i in range(0,len(header)):
            if header[i].startswith(">"):
                count += 1
    print(str(count))
    return count

aa_function(seq,header)
mcount(seq)
seqcount(header)

#provided assertions
assert mcount(seq) == 68
assert seqcount(header) == 84
