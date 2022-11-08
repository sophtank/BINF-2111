#!/usr/bin/env python3
seq = "MSRSLLRFLLFLLLLPPLP"
M = "M"
R = "R"
L = "L"
Y = "Y"
def aa_function(seq,res):
    percent = round((seq.count(res) / len(seq)) * 100)
    print(str(percent))
    return percent


aa_function(seq, M)
aa_function(seq, R)
aa_function(seq, L)
aa_function(seq, Y)

assert aa_function(seq, M) == 5
assert aa_function(seq, R) == 11
assert aa_function(seq, L) == 47
assert aa_function(seq, Y) == 0