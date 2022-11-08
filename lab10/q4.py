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

seq = []

for line in lines:
        line = line.rstrip()

        if line[0] != '>':
            seq.append(line)

def counts():
    for i in range(0,len(seq)):
        #AT and GC counts
        AT = seq[i].count("A") + seq[i].count("T")
        print("Amount of AT: " + str(AT))
        GC = seq[i].count("G") + seq[i].count("C")
        print("Amount of GC: " + str(GC))
        total = AT + GC
        ATC = (AT/total) * 100
        GTC = (GC/total) * 100
        GTC = round(GTC, 2)
        ATC = round(ATC, 2)
        print("Your AT content is "+ str(ATC) + "% and your GC content is " + str(GTC) + "%")
        if ATC > 65:
            print("The sequence is high AT.")
        elif ATC <= 65 and ATC > 45:
            print("This sqeuence has medium AT.")
        elif ATC < 0.45:
            print("This sequence has very low AT...")
        else:
            print("ERROR")

counts()