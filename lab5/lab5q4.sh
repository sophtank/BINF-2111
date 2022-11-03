#!/bin/bash

#Write a bash script that count the number of ATG (starts), Serine (S), Arginine (R), and TAA, TAG, TGA (stops)
#from the example2.fasta file then converts them into amino acid M, S, R, and * for TAA, TAG, TGA for stop codon.
#Remember that ATG encodes for methonine so the only count the from the beginning of the sequence or the end for the stops.
#Serine and Arginine can be throughout the sequence.

input=$1

#Methionine ATG
echo "Total amount of Methionine (START)"
grep -o "^ATG" $1 | wc -l

#Serine AGA AGG AGT AGC TCA TCG
echo "Total amount of Serine"
grep -Eo "AGA|AGG|AGT|AGC|TCA|TCG" $1 | wc -l
echo "Amount of AGA"
grep -Eo "AGA" $1 | wc -l
echo "Amount of AGG"
grep -Eo "AGG" $1 | wc -l
echo "Amount of AGT"
grep -Eo "AGT" $1 | wc -l
echo "Amount of AGC"
grep -Eo "AGC" $1 | wc -l
echo "Amount of TCA"
grep -Eo "TCA" $1 | wc -l
echo "Amount of TCG"
grep -Eo "TCG" $1 | wc -l

#Arginine GCA GCG GCT GCC TCT TCC
echo "Total amount of Arginine"
grep -Eo "GCA|GCG|GCT|GCC|TCT|TCC" $1 | wc -l
echo "Amount of GCA"
grep -Eo "GCA" $1 | wc -l
echo "Amount of GCG"
grep -Eo "GCG" $1 | wc -l
echo "Amount of GCT"
grep -Eo "GCT" $1 | wc -l
echo "Amount of GCC"
grep -Eo "GCC" $1 | wc -l
echo "Amount of TCT"
grep -Eo "TCT" $1 | wc -l
echo "Amount of TCC"
grep -Eo "TCT" $1 | wc -l

#STOP TAA TAG TGA
echo "Total amount of STOP"
grep -Eo "TAA$|TAG$|TGA$" $1 | wc -l
echo "Amount of TAA"
grep -Eo "TAA$" $1 | wc -l
echo "Amount of TAG"
grep -Eo "TAG$" $1 | wc -l
echo "Amount of TGA"
grep -Eo "TGA$" $1 | wc -l

#seds
sed "s/^ATG/M/g" $1 | 
sed "s/AGA/S/g" |
sed "s/AGG/S/g" | 
sed "s/AGT/S/g" | 
sed "s/AGC/S/g" |
sed "s/TCA/S/g" | 
sed "s/TCG/S/g" | 
sed "s/GCA/A/g" |
sed "s/GCG/A/g" | 
sed "s/GCT/A/g" | 
sed "s/GCC/A/g" |
sed "s/TCT/A/g" | 
sed "s/TCC/A/g" | 
sed "s/TAA$/*/g" |
sed "s/TAG$/*/g" | 
sed "s/TGA$/*/g"