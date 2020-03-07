import numpy as np

def initgame(seednum=10):
    g = np.zeros([64,64])
    gidx = np.argwhere(g==0)
    seeddraw = np.random.randint(0, high=gidx.shape[0], size=seednum)
    a = gidx[seeddraw]
    g[a[:,0],a[:,1]] = 1
    seedidx = a

    return g, seedidx
