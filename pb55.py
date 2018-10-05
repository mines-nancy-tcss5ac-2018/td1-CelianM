# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:33:44 2018

@author: mullerma1u
"""

def listtoint(li):
    "Turns a list of number strings into an integer"
    n = len(li)
    sum = 0
    for i in range(n):
        sum += (int(li[i]))*(10**(n-1-i))
    return sum

def solve55(n):
    "Solve the 55th Euler problem"
    counter = 0
    for i in range(5,n+1): # 1,2,3,4 are not Lychrel numbers as any n<= 9 is a palindrome
        chn = str(i)
        li = list(chn)
        mirror = list(reversed(li))
        pal = listtoint(mirror)
        c = 0
        while c <= 50 and mirror != li:
            i = i + pal
            chn = str(i)
            li = list(chn)
            mirror = list(reversed(li))
            pal = listtoint(mirror)
            c += 1
        if c > 50 and mirror != li:
            counter += 1
    return counter

assert(solve55(196)>=1) # since 196 is a Lychrel number, there has to be at least 1

print (solve55(10000))