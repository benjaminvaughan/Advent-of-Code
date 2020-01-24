from math import *
import numpy as np
import matplotlib.pyplot as plt

width = 6
height = 25
area = width * height

raw_img = open('day8.txt').read().strip()
img_arr = np.asarray([int(i) for i in raw_img])

n_elements = img_arr.shape[0]

nlayers = int(n_elements / area)

layers = []

for i in range(0, n_elements, area):
    layer = img_arr[i:i+area]
    layers.append(layer)

m = area
ind = 0
for i in range(len(layers)):
    b1 = np.sum(layers[i] == 0)
    if b1 < m:
        m = b1
        ind = i

b2 = np.sum(layers[ind] == 1)
b3 = np.sum(layers[ind] == 2)
ans = b2 * b3

print('the answer to part 1 is %s' % ans)

d_msg = np.zeros((width, height))
for layer in layers:
    layer = np.reshape(layer,(width, height))
    bb = layer == 0
    bw = layer == 1
    bt = layer == 2

    d_msg[bb] = 1
    d_msg[bw] = 0
    
    
    if np.sum(bt) == 0:
        break
    
    new_layers.append(layer)

    
d = {1 : 'white',
     2 : 'black'}
