

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
        self.y_vals.append(arg)
        self.x_vals.append(self.x)

    def down(self, arg):
        self.y_vals.append(-1 * arg)
        self.x_vals.append(self.x)

    def right(self, arg):
        self.y_vals.append(self.y)
        self.x_vals.append(arg)

    def left(self, arg):
        self.y_vals.append(self.y)
        self.x_vals.append(-1 * arg)

    def iterator(self):
        for i in range(len(self.wire)):
            arg = self.wire[i][1::]
            if self.wire[i][0] == 'R':
                self.right(arg)
            elif self.wire[i][0] == 'L':
                self.left(arg)
            elif self.wire[i][0] == 'D':
                self.down(arg)
            elif self.wire[i][0] == 'U':
                self.up(arg)

    def plotter(self):
        pass
        # x = np.asarray(self.x_vals).flatten()
        # y = np.asarray(self.y_vals).flatten()


p = plot_wire(wire1)
