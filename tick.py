import numpy as np
from kernel import kernel
from neighbors import neighbors

def tick(g):

    gp = g

    j = gp>0
    L = np.argwhere(j)
    D = np.argwhere(np.invert(j))

    K_live = kernel(L, space=gp.shape[0])
    K_dead = kernel(D, space=gp.shape[0])

    N_live = neighbors(gp, K_live, L)
    N_dead = neighbors(gp, K_dead, D)

    S_live = np.array([np.sum(n) for n in N_live])
    S_dead = np.array([np.sum(n) for n in N_dead])

    rip = L[np.any([S_live < 2, S_live > 3], axis=0)]
    gp[rip[:,0], rip[:,1]] = 0

    baby = D[S_dead == 3]
    gp[baby[:,0],baby[:,1]] = 1

    return gp
