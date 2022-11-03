#!/usr/bin/env python3

input = 'GAATTCAGTAGATAGTAAGGAATTCTATGTATGTAGGCGCGCGTGCGCGTGCGCGGAATTC'

#count the number of AT repeats
AT = input.count('AT')
print("You have " + str(AT) + " AT repeats.")

#count the number of GC repeats
GC = input.count('GC')
print("You have " + str(GC) + " GC repeats.")

#make sequence into list
listForm = list(input)
print("Creating complement...")

#for loop to go through and make changes
for x in range(len(listForm)):

    #this is messed up but it works. Changed C to Y and then G to C and then Y to G. etc .
    if listForm[x] == 'C':
        listForm[x] = 'Y'

    if listForm[x] == 'A':
        listForm[x] = 'Z'
    
    if listForm[x] == 'G':
        listForm[x] = 'C'

    if listForm[x] == 'Y':
        listForm[x] = 'G'

    if listForm[x] == 'T':
        listForm[x] = 'A'

    if listForm[x] == 'Z':
        listForm[x] = 'T'

print(str(listForm))

eco = input.count('GAATTC')
print('You have ' + str(eco) + ' ecoRI sites. Now cutting...')

ecoCut = input.replace('GAATTC', 'G AATTC')
print(ecoCut)

atcount = input.count('A') + input.count('T')
print('Your AT count is ' + str(atcount))

gccount = input.count('G') + input.count('C')
print('Your GC count is ' + str(gccount))

rna = input.replace('T','U')
print('Replacing all Ts with Us. ' + str(rna))




