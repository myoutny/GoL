%load_ext autoreload
%autoreload 2

import numpy as np
from kernel import kernel
import matplotlib.pyplot as plt
from time import sleep

A = np.random.randint(1,10,[6,6])
A
loc = np.array([2,3])
order = 3
for k in range(order):
    dx = np.arange(loc[0]-order+k, loc[0]+order+1-k)
    dy = np.arange(loc[1]-order+k, loc[1]+order+1-k)
    ix = np.mod(dx,6)
    iy = np.mod(dy,6)
    print(ix)
k = kernel(np.array([[3,3]]), type='square', order=0, space=8)
k[:,:,0]

a=[]
r = 5
for t in range(360):
    x = 3+np.round(r*np.cos(t*np.pi/180))
    y = 3+np.round(r*np.sin(t*np.pi/180))
    a.append(np.array([x,y]))

# for o in range(10):
#     kin = kernel(np.array([[33,33]]), type='circle', order=o, space=64)
#     plt.imshow(kin[:,:,0])
#     plt.show()


space = 24
order = 5
h = np.zeros([space,space])
v = np.indices(h.shape)
c = [12,21]
ia = (v[0] - c[0])
ib = (v[1] - c[1])
mia = np.mod(ia,space)
mib = np.mod(ib,space)
h = (ia**2. + ib**2.) <= order**2.0
ia
mia
plt.imshow(h)










kin = kernel(np.array([[12,12]]), type='circle', order=5, space=24)
plt.imshow(kin[:,:,0])

A = np.random.randint(0,10,[8,8])


k = kernel(np.array([[12,17]]), type='circle', order=5, space=24)
plt.imshow(k[:,:,0])
plt.imshow(h)

order = 12
c = [,22]
space = 24

p1,p2 = np.indices([space,space])
br = [c[0] - order/2., c[0] + order/2.]
bc = [c[1] - order/2., c[1] + order/2.]
mbr = np.mod(br,space)
mbc = np.mod(bc,space)

if np.all(mbr == br):
    h1 = (p1>=br[0]) & (p1<=br[1])
else:
    h1 = (p1>=br[0]) | (p1<=br[1])

if np.all(mbc == bc):
    h2 =  (p2>=bc[0]) & (p2<=bc[1])
else:
    h2 =  (p2>=bc[0]) | (p2<=bc[1])

h = h1 & h2
plt.imshow(h)



o = 4.
aa = (vv[0] - 12.)**2. + (vv[1] - 12.)**2. <= o**2.0
plt.imshow(aa)
plt.show()
2./36.
# c = np.unique(np.vstack(a),axis=0).astype(int)
# B = np.zeros([12,12])
# B[c[:,0], c[:,1]]=1
# D = ((B + kin[:,:,0]) > 0).astype(int)
# D
