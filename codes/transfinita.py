import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1],'rt')

nx = int(f.readline())
rt = np.zeros((nx,2))
for i in range(nx):
    l=f.readline()
    rt[i,0]=l.split(' ')[0]
    rt[i,1]=l.split(' ')[1]

n2 = int(f.readline())

if (n2 != nx):
    print("top and botton discretization should match")
    sys.exit(0)

rb = np.zeros((nx,2))
for i in range(nx):
    l=f.readline()
    rb[i,0]=l.split(' ')[0]
    rb[i,1]=l.split(' ')[1]

ny = int(f.readline())
rl = np.zeros((ny,2))
for i in range(ny):
    l=f.readline()
    rl[i,0]=l.split(' ')[0]
    rl[i,1]=l.split(' ')[1]

n2 = int(f.readline())

if (n2 != ny):
    print("left and right discretization should match")
    sys.exit(0)

rr = np.zeros((ny,2))
for i in range(ny):
    l=f.readline()
    rr[i,0]=l.split(' ')[0]
    rr[i,1]=l.split(' ')[1]

f.close()

gridx = np.zeros((ny,nx))
gridy = np.zeros((ny,nx))

gridx[0,:]=rb[:,0]
gridx[ny-1,:]=rt[:,0]
gridx[:,0]=rl[:,0]
gridx[:,nx-1]=rr[:,0]

gridy[0,:]=rb[:,1]
gridy[ny-1,:]=rt[:,1]
gridy[:,0]=rl[:,1]
gridy[:,ny-1]=rr[:,1]

dx = 1.0/nx
dy = 1.0/ny
for j in range(1,ny-1):
    for i in range(1,nx-1):
        idx = i*dx
        jdy = j*dy
        gridx[j,i] = (1.0-idx)*rl[j,0] + idx*rr[j,0] + (1.0 - jdy)*rb[i,0] + jdy*rt[i,0] - (1.0-idx)*(1.0-jdy)*rb[0,0] - (1.0 - idx)*jdy*rt[0,0] - idx*(1.0-jdy)*rb[nx-1,0] - idx*jdy*rt[nx-1,0]
        gridy[j,i] = (1.0-idx)*rl[j,1] + idx*rr[j,1] + (1.0 - jdy)*rb[i,1] + jdy*rt[i,1] - (1.0-idx)*(1.0-jdy)*rb[0,1] - (1.0 - idx)*jdy*rt[0,1] - idx*(1.0-jdy)*rb[nx-1,1] - idx*jdy*rt[nx-1,1]

for i in range(nx):
    plt.plot(gridx[i,:],gridy[i,:],color='gray')
for i in range(ny):
    plt.plot(gridx[:,i],gridy[:,i],color='gray')

plt.plot(rt[:,0],rt[:,1])
plt.plot(rb[:,0],rb[:,1])
plt.plot(rl[:,0],rl[:,1])
plt.plot(rr[:,0],rr[:,1])
plt.show()
