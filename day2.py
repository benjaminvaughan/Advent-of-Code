from math import *


class IntCodeComputer():
    def __init__(self, filename):
        self.filename = filename
        
    def read_file(self):
        incode = []
        f_obj = open(self.filename)
        for line in f_obj:
            split = line.split(',')
            for i in range(0, len(split)):
                incode.append((int(split[i])))
        f_obj.close()
        return incode
                
    def specific_check(self, num1, num2):
        testcode = self.read_file()
        testcode[1] = num1
        testcode[2] = num2
        opcode_ans = self.opcode_check(testcode)
        ans = opcode_ans[0]
        print(ans, 'part 1 answer')

    def search_for_vals(self):
        for i in range(99):
            for j in range(99):
                testcode = self.read_file()
                testcode[1] = i
                testcode[2] = j
                ans_opcode = self.opcode_check(testcode)
                print(ans_opcode[0])
                if ans_opcode[0] == 19690720:
                    print(100 * i + j, 'answer to part 2')
                    return
    def opcode_check(self,opcode):
        for i in range(0, len(opcode), 4):
            pos1 = opcode[i + 1]
            pos2 = opcode[i + 2]
            pos3 = opcode[i + 3]
            if opcode[i] == 1:
                sum = opcode[pos1] + opcode[pos2]
                opcode[pos3] = sum
            elif opcode[i] == 2:
                multiple = opcode[pos1] * opcode[pos2]
                opcode[pos3] = multiple
            elif opcode[i] == 99:
                print('F')
                break

        return opcode




c = IntCodeComputer('day2.txt')
c.specific_check(12, 2)
c.search_for_vals()
