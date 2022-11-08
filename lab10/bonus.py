#!/usr/bin/env python3

username = str(input("Enter username\n"))
username = username.rstrip()

def namecheck(username):
    if username == "Jackson":
        print("Access granted.")
        return(True)
    elif username == "Sophie":
        print("Access granted.")
        return(True)
    elif username == "Kevin":
        print("Access granted.")
        return(True)
    else:
        print("DENIED.")
        return(False)

namecheck(username)

test1 = "Jackson"
test2 = "Bob"
test3 = "Sophie"

print("Assertion Checks:")
assert namecheck(test1) == True
assert namecheck(test2) == False
assert namecheck(test3) == True