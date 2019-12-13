import numpy as np
import matplotlib.pyplot as plt

f_obj = open('day3.txt')

wires = []
for line in f_obj:
    wires.append(line)
f_obj.close()

wire1 = wires[0].split(',')
wire2 = wires[1].split(',')


class plot_wire():
    def __init__(self, wire):
        self.wire = wire
        self.x_vals = []
        self.y_vals = []
        self.x = 0
        self.y = 0
        self.iterator()

    def up(self, arg):
        arg = float(arg)
        _ = [self.y_vals.append(self.y + i) for i in range(int(arg))]
        _ = [self.x_vals.append(self.x) for i in range(int(arg))]
        self.y = arg + self.y

    def down(self, arg):
        arg = float(arg)
        _ = [self.y_vals.append(self.y - i) for i in range(int(arg))]
        _ = [self.x_vals.append(self.x) for i in range(int(arg))]
        self.y = -1 * arg + self.y

    def right(self, arg):
        arg = float(arg)
        _ = [self.x_vals.append(self.x + i) for i in range(int(arg))]
        _ = [self.y_vals.append(self.y) for i in range(int(arg))]
        self.x = arg + self.x

    def left(self, arg):
        arg = float(arg)
        _ = [self.x_vals.append(self.x - i) for i in range(int(arg))]
        _ = [self.y_vals.append(self.y) for i in range(int(arg))]
        self.x = - 1 * arg + self.x

    def iterator(self):
        for i in range(len(self.wire)):
            print(self.wire[i])
            arg = self.wire[i][1::]
            if self.wire[i][0] == 'R':
                self.right(arg)
            elif self.wire[i][0] == 'L':
                self.left(arg)
            elif self.wire[i][0] == 'D':
                self.down(arg)
            elif self.wire[i][0] == 'U':
                self.up(arg)




p1 = plot_wire(wire1)
p2 = plot_wire(wire2)

x1, y1 = p1.x_vals, p1.y_vals
x2, y2 = p2.x_vals, p2.y_vals

coords1 = list(zip(x1, y1))
coords2 = list(zip(x2, y2))

intercepts = list(set(coords1).intersection(set(coords2)))

x = [inter[0] for inter in intercepts]
y = [inter[1] for inter in intercepts]


abs_sum = [abs(abs(intercepts[i][0]) + abs(intercepts[i][1])) for i in range(len(intercepts))]
sum_sort = sorted(abs_sum)
print(sum_sort[1], 'part 1 answer')

wire1_step = [coords1.index(inter) for inter in intercepts]
wire2_step = [coords2.index(inter) for inter in intercepts]

sum_steps = [wire1_step[i] + wire2_step[i] for i in range(len(wire1_step))]

step_sort = sorted(sum_steps)
print(step_sort[1], 'part 2 answer')


plt.scatter(x, y, marker='x', label='intercept', c='red')
plt.plot(x1, y1, label='wire 1')
plt.plot(x2, y2, label='wire 2')
plt.legend()
plt.show()
