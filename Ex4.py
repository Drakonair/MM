import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Ex3
from math import exp
from scipy.special import gamma

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
a = "R0".translate(SUB)
Sval = []
lI = {}
lR = {}
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_19-covid-Confirmed_archived_0325.csv')
d = pd.DataFrame(df)
c = d.columns[4:]
for j in c:
     I = 0
     for i in range(0,len(d['Lat'])):
          if d['Country/Region'][i] == 'US':
               I += ((d[j][i]) if str(d[j][i]).isnumeric() else 0)
          lI[j] = I
df1 = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_19-covid-Recovered_archived_0325.csv')
d1 = pd.DataFrame(df1)
for j in c:
     R = 0
     for i in range(0,len(d1['Lat'])):
          if d1['Country/Region'][i] == 'US':
               R += ((d1[j][i]) if str(d1[j][i]).isnumeric() else 0)
          lR[j] = R
for x in range(len(Ex3.lb)):
     b,g = Ex3.lb[x], Ex3.lg[x]
     for i in c:
          X = lI[i]+lR[i]
     S = (g**b)*X**(b-1)*exp((-1)*g*X)/gamma(b)
     Sval.append(S)
sum = 0
count = 0
print(Sval)
for x in Sval:
     if x!=float('inf'):
          sum+=x
          count+=1
print(sum/count)

