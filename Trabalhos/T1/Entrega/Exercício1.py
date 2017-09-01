# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:29:35 2017

@author: vinicius
"""

import numpy as np
import matplotlib.pyplot as plt


f = open('naca0012','rt')
nx = len(f.readlines())

a = np.zeros((nx,2))
f = open('naca0012','rt')
for i in range(nx):
    l=f.readline()
    a[i,0]=float(l.split(' ')[0])
    a[i,1]=float(l.split(' ')[-1])

#Dimenções:
neta = len(a)
nxi = len(a)

b = [0]*(nxi + 1)
d = [0]*(nxi + 1)
c = [0]*(neta + 1)


"""Esfera"""

#raio da circunferencia, centro no bordo de ataque
#r = 10 # tem que coincidir com o comp

#for i in range(neta+1):
#    c[i] = [r*np.cos(2*i*np.pi/neta) ,r*np.sin(2*i*np.pi/neta)]

"""Retangular"""
l1 = 20
l2 = 20
perimetro = 2*l1 + l2*2
dp = perimetro/neta
peri = 0
for i in range(neta +1):
    if peri < l2/2:
        c[i]=[l1/2, peri]
        peri+= dp
    elif peri < l2/2 + l1:
        c[i]=[l1/2 -(peri-l2/2), l2/2]
        peri+= dp
    elif peri < 3*l2/2 + l1:
        c[i]=[-l1/2,l2/2 - (peri - l2/2 -l1)]
        peri+= dp
    elif peri < 3*l2/2 + 2*l1:
        c[i]=[-l1/2 + (peri - 3*l2/2 - l1), -l2/2 ]
        peri+= dp
    else:
        c[i]=[l1/2, -l2/2 +(peri - 3*l2/2 - 2*l1) ]
        peri+= dp

#distância dos bordos b e d
comp = 9

for i in range(nxi+1):
    b[i] = [1+ i*comp/nxi,0]
    d[i] = [1 + i*comp/nxi,0]
    
    
plt.plot([x[0] for x in a],[x[1] for x in a])
plt.plot([x[0] for x in b],[x[1] for x in b])
plt.plot([x[0] for x in c],[x[1] for x in c])
plt.plot([x[0] for x in d],[x[1] for x in d])
plt.show()

f = open('perfil.txt','wt')

#top
f.write(str(len(a)))
f.write('\n')
for i in range(neta):
    f.write("{:.7f}".format(c[i][0]))
    f.write(' ')
    f.write("{:.7f}".format(c[i][1]))
    f.write('\n')

#b
f.write(str(neta))
f.write('\n')
for i in range(neta):
    f.write("{:.7f}".format(a[i][0]))
    f.write(' ')
    f.write("{:.7f}".format(a[i][1]))
    f.write('\n')

#l
f.write(str(nxi))
f.write('\n')
for i in range(nxi):
    f.write("{:.7f}".format(b[i][0]))
    f.write(' ')
    f.write("{:.7f}".format(b[i][1]))
    f.write('\n')

#r
f.write(str(nxi))
f.write('\n')
for i in range(nxi):
    f.write("{:.7f}".format(d[i][0]))
    f.write(' ')
    f.write("{:.7f}".format(d[i][1]))
    f.write('\n')

f.close()
