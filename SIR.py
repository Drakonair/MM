import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

beta = 2
gamma = 0.5
S0 = 800
I0 = 7
R0 = 0
N = 1000
t = np.linspace(0,8,8)

def d(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

y0 = S0, I0, R0
ret = odeint(d, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

fig = plt.figure(facecolor='w')
g = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
g.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
g.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
g.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered')
g.set_xlabel('Time unit')
g.set_ylabel('Population fraction')
g.set_ylim(0,1.2)
g.yaxis.set_tick_params(length=0)
g.xaxis.set_tick_params(length=0)
g.grid(b=True, which='major', c='w', lw=2, ls='--')
legend = g.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    g.spines[spine].set_visible(False)
plt.show()