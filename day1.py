from math import *
import numpy as np

f_obj = open('day1.txt')

fuel_vals = []
for line in f_obj:
    m = float(line)
    fuel = floor ( m / 3.) - 2
    fuel_vals.append(fuel)

ans = np.sum(fuel_vals)
print(ans, 'answer to part 1')

def HUH(lister):
    print(lister, 'lister')
    out_lister = []
    print(len(lister))
    for i in range(len(lister)):
        fuel = floor ( lister[i] / 3.) - 2
        if fuel > 0:
            out_lister.append(fuel)
    return out_lister

total = ans
while len(fuel_vals) != 0:
    fuel_vals = HUH(fuel_vals)
    total += np.sum(fuel_vals)

print(total, 'answer to part 2')

f_obj.close()

f_obj = open('day1_output.txt', 'w')
for i in range(len(fuel_vals)):
    f_obj.write(str(fuel_vals[i]) + '\n')

f_obj.close()
