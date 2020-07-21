import matplotlib.pyplot as plt
import math
import numpy as np

# Susceptible equation
def fS(N, S, I, beta):
    return -beta*S*I

# Infected equation
def fI(N, S, I, beta, gamma):
    return beta*S*I - gamma*I

# Recovered/deceased equation
def fR(N, I, gamma):
    return gamma*I

def SIR(t, beta, gamma, I0, R0, N, delta, t0 = 0):
    while t0 < t:
        S0 = N - I0 - R0
        S0 += fS(N,S0,I0,beta)*delta
        R0 += fR(N,I0,gamma)*delta
        I0 += fI(N,S0,I0,beta,gamma)*delta
        t0 += delta
    return S0,I0,R0

a,b,c = SIR(1,0.002,0.5,7,0,807,1,0)
print(a,b,c)

    