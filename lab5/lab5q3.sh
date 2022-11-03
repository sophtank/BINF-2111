#!/bin/bash

#3. Write a bash script or command to find sequences with >4 N’s in the sequence (MultiN.fastq), 
#have it print the header of the sequence and the sequence itself.

input=$1
grep -B1 '\(.*N\)\{4\}' $1 | more