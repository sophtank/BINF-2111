#!/usr/bin/env python3

#write a for loop that counts the amount of sequences in example2.fasta

#initialize a counting variable starting at 0 for later
count = 0

#creating a for loop to go through and add one to the counting variable when it finds a '>'
DNA = open("example2.fasta")
lines = DNA.readlines()
for i in range(0, len(lines)):
        if lines[i][0] == '>':
            count = (count + 1)

print(count)

#closing files for good coding practice
DNA.close()