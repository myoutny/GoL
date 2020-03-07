# %load_ext autoreload
# %autoreload 2
# %matplotlib notebook
# %reset?

import numpy as np
from initgame import initgame
from visualize import visualize
from propagate import propagate
import pickle
import matplotlib.pyplot as plt
from tick import tick
import time

t = np.arange(100)
g , sidx = initgame(1000)
mode = 'Live'

if mode == 'Store':
    G = propagate(g,t)
    ani = visualize(G)
elif mode == 'Live':
    fig = plt.figure()
    ax = fig.gca()
    fig.show()
    G = g
    # Im = plt.imshow(g)
    # Im.show()
    while 1:
        plt.imshow(G)
        fig.canvas.draw()
        t = time.time()
        G = tick(G)
        elapsed = time.time() - t
        print(elapsed)

        # Im.set_data(G)
        # plt.draw()
else:
    G = pickle.load( open( "G.p", "rb" ) )
    ani = visualize(G)
