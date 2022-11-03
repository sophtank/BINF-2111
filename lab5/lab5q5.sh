#!/bin/bash

#5. Write a bash script that tells me my username, current directory, the location of our desktop directory, and the date/time

echo -n "You are: "
whoami
echo -n "Your current working directory is: " 
pwd
echo -n "Your desktop directory is: " ~/desktop
echo -n "The date and time is: " 
date
