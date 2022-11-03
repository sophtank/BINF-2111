#!/bin/bash
# Oh NO! You tried to saved your file from a text editor and it got corrupted (Corrupted.fq) You must now find where the file is corrupted by looking at what is missing in the file?
#Write a command or script (better) to find the corrupted lines then print their line numbers.
#Describe what is messing in those lines?


var1=$1
var2=$2

diff -u $1 $2

#There are lines missing and added within the corrupted.fq file. The minus signs 
#denote a line that is in MultiN.fastq and not in corrupted.fastq and the addition signs denote where
#there is a line added in corrupted.fastq that is not in MultiN.fastq