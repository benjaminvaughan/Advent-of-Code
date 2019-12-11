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
        self.x_vals = [0]
        self.y_vals = [0]
        self.x = 0
        self.y = 0
        self.iterator()

    def up(self, arg):
        arg = float(arg)
        self.y_vals.append(arg + self.y)
        self.x_vals.append(self.x)
        self.y = arg + self.y

    def down(self, arg):
        arg = float(arg)
        self.y_vals.append(-1 * arg + self.y)
        self.x_vals.append(self.x)
        self.y = -1 * arg + self.y

    def right(self, arg):
        arg = float(arg)
        self.y_vals.append(self.y)
        self.x_vals.append(arg + self.x)
        self.x = arg + self.x

    def left(self, arg):
        arg = float(arg)
        self.y_vals.append(self.y)
        self.x_vals.append(-1 * arg + self.x)
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

plt.plot(x1, y1, label='wire 1')
plt.plot(x2, y2, label='wire 2')
plt.legend()
plt.show()
