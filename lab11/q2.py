#!/usr/bin/env python3

import argparse, re

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

    if line.startswith('>'):
        header.append(line)
    if not line.startswith('>'):
        seq.append(line)
str_seq = ''.join(seq)

def counts():
    ATC = (str_seq.count("A") + str_seq.count("T")) / len(str_seq) * 100
    GCC = 100 - ATC
    total = len(str_seq)
    GCC = round(GCC, 2)
    ATC = round(ATC, 2)
    print("Your AT content is "+ str(ATC) + "% and your GC content is " + str(GCC) + "%")
    print("The length of your genome is " + str(len(str_seq)))

with open(args.output, 'w') as reader:
        ecoRI = len(re.findall(r'CTTAAG',str_seq))
        print("ecoRI sites: " , ecoRI)
        ecoRII = re.split('CTTAAG', str_seq)
        i = 0
        for i in range(0,ecoRI):
            reader.write("\n" + str(header[0]) + "_ecoRI-cut_" + str(i + 1) )
            reader.write("\n" + ecoRII[i])
        
        speI = len(re.findall('ACTAGT',str_seq))
        speII = re.split('ACTAGT',str_seq)
        print("speI sites: " , speI)
        a = 0
        for i in range(0,speI):
            reader.write("\n" + str(header[0]) + "_speI-cut " + str(a + 1))
            reader.write("\n" + speII[i])


counts()