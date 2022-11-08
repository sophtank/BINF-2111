#!/usr/bin/env python3

#splitting the numbers at a space; specifically said to separate with a space for user clarity.
num1, num2 = input("Please enter two numbers and separate them with a space. ").split()

#converting to integers
num1 = (int(num1))
num2 = (int(num2))

#printing out numbers to make sure user knows what they entered.
print("First number: " + str(num1))
print("Second number: " + str(num2))
#function to do calculations so it can be called
def numbercheck():
    a = num1 % 3
    if a == 0:
        print("The first number is divisible by three " + str((num1/3)) + " times.")
    else:
        print("The first number is NOT divisible by three.")

    b = num2 % 3
    if a == 0:
        print("The second number is divisible by three " + str(round((num2/3), 1)) + " times.")
    else:
        print("The second number is NOT divisible by three.")

numbercheck()