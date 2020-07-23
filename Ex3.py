#Metropolis-Hastings
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

lb, lg = [], []
size = 100
i = 0
b0 = abs(np.random.normal(0, 0.1))
g0 = abs(np.random.normal(0, 0.1))
lb.append(b0)
lg.append(g0)
while i<size-1:
     bs = abs(np.random.normal(0, 0.1))
     gs = abs(np.random.normal(0, 0.1))
     q = np.random.uniform(0,1)
     
     r = min(1,(bs*gs)/(b0*g0))
     if (q<r):
          lb.append(bs)
          lg.append(gs)
     else:
          lb.append(b0)
          lg.append(g0)
     i += 1
fig = plt.figure(facecolor='w')
g = fig.add_subplot(111, facecolor='#e0fbfc', axisbelow=True)
g.plot(np.linspace(0,size,size), lb, 'c', lw=2, label='Beta')
g.plot(np.linspace(0,size,size), lg, 'm', lw=2, label='Gamma')
g.set_xlim(0)
g.set_ylim(0)
g.yaxis.set_tick_params(length=0)
g.xaxis.set_tick_params(length=0)
g.grid(b=True, which='major', c='w', lw=2, ls='solid')
l = g.legend()
l.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
     g.spines[spine].set_visible(False)
plt.title("Beta and Gamma values", size=20)
plt.show()

