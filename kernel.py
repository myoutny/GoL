import numpy as np

def kernel(loc=np.zeros([1,2]), type='square', order=1, space=64):

    H = np.zeros([space,space,loc.shape[0]])
    count = 0
    for c in loc:
        h = np.zeros([space,space])
        if type == 'circle':
            v = np.indices(h.shape)
            h = ((v[0] - c[0])**2. + (v[1] - c[1])**2.) <= order**2.0
            # for r in range(order):
            #     a=[]
            #     for t in range(360):
            #         x = c[0]+np.round(r*np.cos(t*np.pi/180))
            #         y = c[1]+np.round(r*np.sin(t*np.pi/180))
            #         x = np.mod(x,space)
            #         y = np.mod(y,space)
            #         a.append(np.array([x,y]))
            #
            #     cind = np.unique(np.vstack(a),axis=0).astype(int)
            #     h[cind[:,0], cind[:,1]]=1
            # h = ((h) > 0).astype(int)

        else:
            p1,p2 = np.indices(h.shape)
            br = [c[0] - order, c[0] + order]
            bc = [c[1] - order, c[1] + order]
            mbr = np.mod(br,space)
            mbc = np.mod(bc,space)

            if np.all(mbr == br):
                h1 = (p1>=mbr[0]) & (p1<=mbr[1])
            else:
                h1 = (p1>=mbr[0]) | (p1<=mbr[1])

            if np.all(mbc == bc):
                h2 =  (p2>=mbc[0]) & (p2<=mbc[1])
            else:
                h2 =  (p2>=mbc[0]) | (p2<=mbc[1])

            h = h1 & h2
            # dy1 = (c[0]-int(order))
            # dy2 = (c[0]+int(order)+1)
            # dx1 = (c[1]-int(order))
            # dx2 = (c[1]+int(order)+1)
            # v1 = np.mod(np.arange(dy1,dy2),space).tolist()
            # v2 = np.mod(np.arange(dx1,dx2),space).tolist()
            # h[np.ix_(v1,v2)] = 1

        H[:,:,count] = h
        count+=1


    return H
