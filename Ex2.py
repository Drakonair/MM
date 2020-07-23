'''SIR model'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Declaring differential equations
def func(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

#Solving the equations
def SIR(t: np.linspace, beta, gamma, S0, I0, R0, N):
    y0 = S0, I0, R0
    ret = odeint(func, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    return S,I,R

#Plotting the diagram
def plot(t: np.linspace, beta, gamma, S0, I0, R0, N):
    S, I, R = SIR(t, beta, gamma, S0, I0, R0, N)
    fig = plt.figure(facecolor='w')
    g = fig.add_subplot(111, facecolor='#e0fbfc', axisbelow=True)
    g.plot(t, S/N, 'r', lw=2, label='Susceptible')
    g.plot(t, I/N, 'g', lw=2, label='Infected')
    g.plot(t, R/N, 'b', lw=2, label='Recovered')
    g.set_xlim(0,max(t))
    g.set_ylim(0,max(max(S/N),max(I/N),max(R/N))+0.02)
    g.yaxis.set_tick_params(length=0)
    g.xaxis.set_tick_params(length=0)
    g.set_xlabel('Time unit')
    g.set_ylabel('Population fraction')
    g.grid(b=True, which='major', c='w', lw=2, ls='solid')
    l = g.legend()
    l.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        g.spines[spine].set_visible(False)
    plt.title("SIR model", size=20)
    plt.show()

#Example
plot(np.linspace(0,8,8),2,0.5,800,7,0,1000)