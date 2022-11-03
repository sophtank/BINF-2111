#!/bin/bash
# Write a bash script that prints any range of lines you give it from a file.
#For example, bash script.sh file.tsv (prints lines 2 to 5). Place code here and make an executable script.


num1=$1
num2=$2
file=$3


sed -n "$1,$2p" $file
