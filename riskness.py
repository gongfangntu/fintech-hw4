import math
import cmath
from sympy import *
import numpy as np
import pandas as pd
from scipy.optimize import fsolve
from pandas import DataFrame


df = pd.read_csv('weekly.csv')

#print(df)

df = df.iloc[:, 1:]
print(df)

riskness_list = []
for i in range(39):
	tmp_list = []
	for j in range(158):
		tmp_list.append(df.iloc[j,i])
	x = 0.001
	tmp = 0
	while abs(tmp - 1) > 0.00001:
		tmp = 0
		for j in range(158):
			tmp += (math.exp((-1) * x * tmp_list[j])) / 158
		if tmp < 1:
			x -= 0.00000001
		else:
			x += 0.00000001
	#print(tmp)
	#print(x)
	riskness = math.exp(-1 * x)
	print(riskness)
	riskness_list.append(riskness)

sorted_riskness_list = sorted(riskness_list)
rank = []
for i in range(39):
	rank.append(i + 1)

name_list = []
df = pd.read_csv('weekly.csv')
for i in df:
	if i == "Date":
		pass
	else:
		name_list.append(i)

print(name_list)
sorted_name_list = []
for i in (sorted(range(len(riskness_list)), key=lambda k: riskness_list[k])):
	sorted_name_list.append(name_list[i])
print(sorted_name_list)
Risk = {
		"Rank": rank,
		"ETF" : sorted_name_list
}
df = DataFrame(Risk, columns= ['Rank', 'ETF'])
export_csv = df.to_csv("riskness_week.csv")
		
