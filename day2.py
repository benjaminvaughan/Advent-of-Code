from math import *

opcode = []
f_obj = open('day2.txt')
for line in f_obj:
    split = line.split(',')
    for i in range(0, len(split), 4):
        opcode.append((split[i:i+4]))

f_obj.close()
for i in range(len(opcode)):
    #find the index of position 1 in our data strcture
    pos1 = int(opcode[i][1])
    ind11 = floor(pos1 / 4)
    ind12 = pos1 % 4
    #find the index of position 2 in our data structure
    pos2 = int(opcode[i][2])
    ind21 = floor(pos2 / 4)
    ind22 = pos2 % 4
    #find the index of position 3 in our data structure
    pos3 = int(opcode[i][3])
    ind31 = floor(pos3 / 4)
    ind32 = pos3 % 4
    #do operations.
    if opcode[i][0] == '1':
        sum = int(opcode[ind11][ind12]) + int(opcode[ind21][ind22])
        opcode[ind31][ind32] = sum
    if opcode[i][0] == '2':
        multiple = int(opcode[ind11][ind12]) * int(opcode[ind21][ind22])
        opcode[ind31][ind32] = multiple
    if opcode[i][0] == '99':
        print('hit 99 program is halting')
        break

f_obj = open('day2_output.txt', 'w')

for i in range(len(opcode)):
    for j in range(len(opcode[i])):
        f_obj.write(str(opcode[i][j]) + ',')
