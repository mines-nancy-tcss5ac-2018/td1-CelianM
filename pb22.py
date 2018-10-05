# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

f = open("p022_names.txt","r")
buffer = []
for line in f:
    buffer.append(line)
li = buffer[0].split(',')
li.sort()

def solve(li):
    "Solve the 22nd Euler problem"
    sum = 0
    for i in range(len(li)):
        string = li[i]
        rank = i+1
        charsum = 0
        for char in string:
            charsum += (ord(char)-64)
        sum += rank*charsum
    return sum

print(solve(li))