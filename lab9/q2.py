#!/usr/bin/env python3


DNA = open("example2.fasta")
lines = DNA.read()

#Import the example2.fasta file.

#In the script make these as functions!

#a) Count the number of ‘AT repeats’
def AT_repeats():
    repeats = lines.count('AT')
    print("You have " + str(repeats) + " AT repeats.")

AT_repeats()

#b) Count the number of ‘GC repeats’
def GC_repeats():
    repeats = lines.count('GC')
    print("You have " + str(repeats) + " GC repeats.")

GC_repeats()

#c) Count the length of each sequence
def seqlength():
    DNA = open("example2.fasta")
    listForm = DNA.readlines()
    for x in listForm:
        if x.startswith('ATG'):
            print(x + "length: " + str(len(x)))

seqlength()

#d) Count the number of EcoR1 sites (G*AATTC)

def ecor1():
    eco = lines.count('GAATTC')
    print(str(eco) + " ecoR1 sites found.")

ecor1()

#e) Replaces all T with U and prints to new file called RNA converted
def RNA():
    replacing = lines.replace("T","U")
    print(replacing)
    f = open("RNA_converted" , "w")
    f.write(replacing)
RNA()

#f) Counts AT and GC content
def content():
    AT = lines.count("A") + lines.count("T")
    print("Amount of AT: " + str(AT))
    GC = lines.count("G") + lines.count("C")
    print("Amount of GC: " + str(GC))
    total = AT + GC
    ATC = (AT/total) * 100
    GTC = (GC/total) * 100
    GTC = round(GTC, 2)
    ATC = round(ATC, 2)
    print("Your AT content is "+ str(ATC) + "% and your GC content is " + str(GTC) + "%")
content()

DNA.close()
