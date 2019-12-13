from math import *
import numpy as np

pasti = str(284639)

possible = []

def check_increase(num):
    num = str(num)
    for j in range(1, 6):
        if num[j-1] <= num[j]:
            continue
        else:
            return False
    return num


def check_double(num):
    num = str(num)
    for i in range(10):
        if num.count(str(i)) >= 2:
            return num
    return False

def check_double_part_2(num):
    num = str(num)
    for i in range(10):
        if num.count(str(i)) == 2:
            return num
    return False

for i in range(284639, 748759):
    num = check_increase(i)
    if num is not False:
        num = check_double(num)
        if num is not False:
            possible.append(num)

for i in range(284639, 748759):
    num = check_increase(i)
    if num is not False:
        num = check_double_part_2(num)
        if num is not False:
            possible.append(num)
print(len(possible))



