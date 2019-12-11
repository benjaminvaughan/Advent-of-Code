from math import *

f_obj = open('day1.txt')

fuel_vals = []
for line in f_obj:
    m = float(line)
    fuel = floor ( m / 3.) - 2
    fuel_vals.append(fuel)

f_obj.close()

f_obj = open('day1_output.txt', 'w')
for i in range(len(fuel_vals)):
    f_obj.write(str(fuel_vals[i]) + '\n')

f_obj.close()
