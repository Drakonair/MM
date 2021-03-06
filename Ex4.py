import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Ex3
from math import exp
from scipy.special import gamma

S = 0
Sval = [] #pi(X|\beta,\gamma) values
lI = {} #infected
lR = {} #recovered

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_19-covid-Confirmed_archived_0325.csv')
d = pd.DataFrame(df) #infected Data

c = d.columns[4:] #store dates

for j in c: #calculate Infected for each day
     I = 0
     for i in range(0,len(d['Lat'])):
          if d['Country/Region'][i] == 'US':
               I += ((d[j][i]) if str(d[j][i]).isnumeric() else 0)
          lI[j] = I

df1 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_19-covid-Recovered_archived_0325.csv')
d1 = pd.DataFrame(df1) #recovered Data

for j in c: #calculate Recovered for each day
     R = 0
     for i in range(0,len(d1['Lat'])):
          if d1['Country/Region'][i] == 'US':
               R += ((d1[j][i]) if str(d1[j][i]).isnumeric() else 0)
          lR[j] = R

for x in range(len(Ex3.lb)):
     b,g = Ex3.lb[x], Ex3.lg[x]
     for i in c:
          X = lI[i]+lR[i]
          S *= (g**b)*X**(b-1)*exp((-1)*g*X)/gamma(b)
     Sval.append(S)
     S = 0

R_0 = 0
for x in range(len(Ex3.lb)):
     R_0 += Ex3.lb[x]/Ex3.lg[x]*Sval[x]
