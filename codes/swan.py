import sys
import numpy as np

t = np.linspace(0,1,30)

rt = 1.0 - 3.0*t + 3.0*np.power(t,2)
rr = 1.0 + 2.0*(1.0 - t) -2*np.power(1.0-t,2)

f = open('swan.txt','wt')

n = t.shape[0]
f.write(str(n))
f.write('\n')
for i in range(n):
    f.write("{:.2f}".format(t[i]))
    f.write(' ')
    f.write("{:.2f}".format(rt[i]))
    f.write('\n')

f.write(str(n))
f.write('\n')
for i in range(n):
    f.write("{:.2f}".format(t[i]))
    f.write(' ')
    f.write("{:.2f}".format(0.0))
    f.write('\n')

f.write(str(n))
f.write('\n')
for i in range(n):
    f.write("{:.2f}".format(0.0))
    f.write(' ')
    f.write("{:.2f}".format(t[i]))
    f.write('\n')

f.write(str(n))
f.write('\n')
for i in range(n):
    f.write("{:.2f}".format(rr[i]))
    f.write(' ')
    f.write("{:.2f}".format(t[i]))
    f.write('\n')

f.close()
