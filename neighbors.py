# Input: map, kernel set and population indices
# Output: neighbors of each pop based on type of kernel

import numpy as np

def neighbors(g, K, pop):
    N = []
    c = 0
    for p in pop:
        kidx = np.argwhere(K[:,:,c])
        center = np.all(kidx==p,axis=1)
        nidx = kidx[np.invert(center),:]
        n = g[nidx[:,0],nidx[:,1]]
        N.append(n)
        c += 1

    return N
