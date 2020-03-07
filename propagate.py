import numpy as np
from tick import tick
import pickle

def propagate(g,t):

    G = np.zeros([len(t), g.shape[0], g.shape[1]])

    for k in t:
        if k == 0:
            G[k,:,:] = g
        else:
            G[k,:,:] = tick(G[k-1,:,:])

    pickle.dump( G, open( "G.p", "wb" ) )
    return G
