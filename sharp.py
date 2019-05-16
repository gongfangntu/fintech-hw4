import math
import cmath
from sympy import *
import numpy as np
import pandas as pd
from scipy.optimize import fsolve
from pandas import DataFrame
def F(i):
	a, b, c, d = i[0], i[1], i[2], i[3]
	#print(a,b,c,d)
	e = cmath.sqrt(a ** 2 - b ** 2)
	f = cmath.sqrt(d * e)
	#print(mean)
	return [ 
	c + d * b / e - mean, 
	d * (a ** 2) / (e ** 3) - variance, 
	3 * b / (a * f) - sk, 
	3 + (3 / (d * e)) * (1 + 4 * ((b / a) ** 2)) - kurt
   ]
def main():
	sharp_list = []
	global mean, variance, sk, kurt
	df = pd.read_csv('weekly.csv')
	#print(df.iloc[:,1:])
	df = df.iloc[:,1:]
	for i in range(39):
		global tmp_list
		tmp_list = []
		for j in range(158):
			tmp_list.append(df.iloc[j, i])
	#print(tmp_list)
		tmp = 0
		for j in range(158):
			tmp += tmp_list[j]
		mean = tmp / 37
		tmp = 0
		for j in range(158):
			tmp += (tmp_list[j] - mean) ** 2
		variance = tmp / 37
		tmp = 0
		sk = 3 * (mean - np.median(tmp_list)) / np.std(tmp_list)
		tmp = 0
		for j in range(158):
			tmp += (tmp_list[j] - mean) ** 4
		tmp /= 37
		tmp /= (np.std(tmp_list) ** 4)
		kurt = tmp - 3
		#print(kurt)
		r = fsolve(F, [ 1, 1, 1, 1])
		return_value = np.median(tmp_list)
		a, b, c, d = r[0], r[1], r[2], r[3]
		f = 3
		e = (1 / f) * (b + (a * (c - return_value)) / math.sqrt(d ** 2 + (c - return_value) ** 2))

		sharp = math.sqrt(2 * (f * e * (c - return_value) - d * (math.sqrt(a ** 2 - b ** 2) - math.sqrt(a ** 2 - (b - f * e) ** 2))))
		sharp_list.append(sharp)
	print(sorted(sharp_list))
	print(sorted(range(len(sharp_list)), key=lambda k: sharp_list[k]))
	df = pd.read_csv('monthly.csv')
	name_list = []
	for i in df:
		if i == "Date":
			pass
		else:
			name_list.append(i)
	print(name_list)
	sorted_name_list = []
	for i in (sorted(range(len(sharp_list)), key=lambda k: sharp_list[k])):
		sorted_name_list.append(name_list[i])
	print(sorted_name_list)
	sorted_name_list = sorted_name_list[::-1]
	print(len(sorted_name_list))
	rank = []
	for i in range(39):
		rank.append(i + 1)
	Sharp = {
		"Rank": rank,
		"ETF" : sorted_name_list
	}
	df = DataFrame(Sharp, columns= ['Rank', 'ETF'])
	export_csv = df.to_csv("sharp.csv")
main()
