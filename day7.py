import time
from itertools import permutations


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
                
    def specific_check(self, num1=None, num2=None, id=1, part=None):
        testcode = self.read_file()
        if num1 is not None and num2 is not None:
            testcode[1] = num1
            testcode[2] = num2
        opcode_ans = self.run_opcode(testcode, id)
        ans = opcode_ans[0]
        print('part %s answer : %s' % (part, ans))

    def search_for_vals(self):
        for i in range(99):
            for j in range(99):
                testcode = self.read_file()
                testcode[1] = i
                testcode[2] = j
                ans_opcode = self.opcode_check(testcode)
                if ans_opcode[0] == 19690720:
                    print(100 * i + j, 'answer to part 2')
                    return

    def four_p_mode(self, opcode, i, fmt_t):
        if fmt_t is None:       
            pos1 = opcode[i + 1]
            pos2 = opcode[i + 2]
            pos3 = opcode[i + 3]
        else:
            p = []
            for j in range(1, len(fmt_t)+1):
                d = { '1' : i + j,
                      '0' : opcode[i + j]}
                p.append(d[fmt_t[j-1]])
            pos1 = p[0]
            pos2 = p[1]
            pos3 = p[2]
        return pos1, pos2, pos3

    def true_false_jump(self, opcode, i, fmt_t):
        if fmt_t is None:       
            pos1 = opcode[i + 1]
            pos2 = opcode[i + 2]
        else:
            p = []
            for j in range(1, len(fmt_t)+1):
                d = { '1' : i + j,
                      '0' : opcode[i + j]}
                p.append(d[fmt_t[j-1]])
            pos1 = p[0]
            pos2 = p[1]
        return pos1, pos2
    
    def in_value_mode(self, opcode, i, value):
        val = value
        pos = opcode[i + 1]
        return val, pos

    def out_value_mode(self, opcode, i, fmt_t):
        if fmt_t is None:       
            pos = opcode[i + 1]
        else:
            p = []
            for j in range(1, len(fmt_t)+1):
                d = { '1' : i + j,
                      '0' : opcode[i + j]}
                p.append(d[fmt_t[j-1]])
            pos = p[0]
        return pos

    def format_check(self, value):
        l = len(value)
        command = value[-1]
        # tuple : 1st param, 2nd param, 3rd param.
        if l == 3:
            return  command, (value[0], '0', '0')
        if l == 4:
            return  command, (value[1], value[0], '0')
        if l == 5:
            return command, (value[2], value[1], value[0])
        return command, None

    def run_opcode(self, opcode, id, phase=None):
        i = 0
        inp = 0
        while opcode[i] != 99:
            num = str(opcode[i])
            cmd, fmt_t = self.format_check(num)
            opcode, i = self.opcode_check(opcode, id, i, cmd, fmt_t, phase=phase, inp=inp)
            if i == False:
                return opcode
            inp += 1
        return opcode

    def amplifier(self, phase, signal):
        testcode = self.read_file()
        opcode_ans = self.run_opcode(testcode, id=signal, phase=phase)
        ans = opcode_ans
        return ans
        
    def opcode_check(self,opcode, id, i, cmd, fmt_t, phase=None, inp=0):
        if cmd == '1':
            pos1, pos2, pos3 = self.four_p_mode(opcode, i, fmt_t)
            sum = opcode[pos1] + opcode[pos2]
            opcode[pos3] = sum
            i += 4
        elif cmd == '2':
            pos1, pos2, pos3 = self.four_p_mode(opcode, i, fmt_t)
            multiple = opcode[pos1] * opcode[pos2]
            opcode[pos3] = multiple
            i += 4
        elif cmd == '3':
            val, pos = self.in_value_mode(opcode, i, id)
            if phase is not None:
                if inp == 0:
                    val = phase
                else:
                    val = id
            opcode[pos] = val
            i += 2
        elif cmd == '4':
            pos = self.out_value_mode(opcode, i, fmt_t)
            return opcode[pos], False
            i += 2
        elif cmd is '5':
            pos1, pos2 = self.true_false_jump(opcode, i, fmt_t)
            if opcode[pos1] != 0:
                instr = opcode[pos2]
                i = instr
            else:
                i += 3
        elif cmd == '6':
            pos1, pos2 = self.true_false_jump(opcode, i, fmt_t)
            if opcode[pos1] == 0:
                instr = opcode[pos2]
                i = instr
            else:
                i += 3
        elif cmd == '7':
            pos1, pos2, pos3 = self.four_p_mode(opcode, i, fmt_t)
            if opcode[pos1] < opcode[pos2]:
                opcode[pos3] = 1
            else:
                opcode[pos3] = 0
            i += 4
        elif cmd == '8':
            pos1, pos2, pos3 = self.four_p_mode(opcode, i, fmt_t)
            if opcode[pos1] == opcode[pos2]:
                opcode[pos3] = 1
            else:
                opcode[pos3] = 0
            i += 4

        return opcode, i


c = IntCodeComputer('day7.txt')
sums = []
ps = []
for p in permutations((range(0,5))):
    ps.append(p)
    sig = 0
    for s in p:
        a = c.amplifier(s, sig)
        sig = a
    sums.append(sig)

ind = sums.index(max(sums))
print(ps[ind])
print(max(sums))

ps = []
sums = []
for p in permutations((range(5,9))):
    ps.append(p)
    sig = 0
    for s in p:
        a = c.amplifier(s, sig)
        sig = a
    sums.append(sig)
