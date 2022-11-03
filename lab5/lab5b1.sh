#!/bin/bash
# Write a bash script that converts this into a tsv file (specific files and all files)?

file1=$1
file2=$2

cat $1 | tr ',' '\t'  > $2