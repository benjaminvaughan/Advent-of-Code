from math import *
import numpy as np


f = open('day6.txt')

d = {}

for line in f:
    line = line.replace('\n', '')
    i, o = line.split(')')
    d[o] = i

def func_of_fun(o, sum):
    while o != 'COM':
        o = d[o]
        sum += 1
    return sum

sum = 0
for o in d.keys():
    sum = func_of_fun(o, sum)
print(sum, 'the answer to part 1')

def find_tree(o):
    nd = {}
    while o != 'COM':
        nd[o] = d[o]
        o = d[o]

    return nd

y = find_tree('YOU')
s = find_tree('SAN')

def find_o_swap(y, s):
    l = []
    for e in y.keys():
        if e in s.keys():
            l.append(e)

    fd = {}
    sums = []
    for e in l:
        o = 'YOU'
        g = 'SAN'
        sum = 0
        while o != e:
            fd[o] = y[o]
            o = y[o]
            sum += 1
        while g != e:
            fd[g] = s[g]
            g = s[g]
            sum += 1
        sums.append(sum)

    return sums

print(np.min(find_o_swap(y, s)), 'the answer to part 2')
