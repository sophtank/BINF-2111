#!/usr/bin/env python3

#opening pUC19c file, creating a list of sequences.
seq = open('pUC19c.fasta')
lines = seq.readlines()
sequence = []
for i in range (0, len(lines)):
    if lines[i][0] != '>':
        sequence.append(lines[i].strip("\n"))

#joining all sequences in the list together.
Sequence = " ".join(sequence)
Sequence = Sequence.rstrip("\t")

#counting amount of SMAI sequences
SMAI = Sequence.count("CCCGGG")
print(str(SMAI) + " SMAI sequences.")

#AT and GC counts
AT = Sequence.count("A") + Sequence.count("T")
print("Amount of AT: " + str(AT))
GC = Sequence.count("G") + Sequence.count("C")
print("Amount of GC: " + str(GC))
total = AT + GC
ATC = (AT/total) * 100
GTC = (GC/total) * 100
GTC = round(GTC, 2)
ATC = round(ATC, 2)
print("Your AT content is "+ str(ATC) + "% and your GC content is " + str(GTC) + "%")