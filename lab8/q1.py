#!/usr/bin/env python3

protein="vlspadknvww"

#uppercase
uppercase = protein.upper()
print('Your sequence is ' + uppercase)

#count the number of valine
valine = uppercase.count('V')
print('You have ' + str(valine) + ' valine')

#count the number of tryptophan
tryp = uppercase.count('W')
print('You have ' + str(tryp) + ' tryptophan' )

#count the length of the sequence
length = len(protein)
print('The length of your sequence is ' + str(length))

#count the number of polar neutral side chains
#SER THR CYS ASN GLU TYR
count = (uppercase.count('S') + uppercase.count('T') + uppercase.count('C') + uppercase.count('N') + uppercase.count('Q') + uppercase.count('Y'))
print('You have ' + str(count) + ' polar neutral side chains.')

replacement = uppercase.replace('W','G')
print('Replace all tryptophan with glycine: ' + replacement)