import pandas as pd

df = pd.read_csv('weekly.csv')
#ret = pd.read_csv('return.csv')
omega = []
names = []

for i, col in enumerate(df):
	if col == 'Date':
		continue

#	rf = float((ret['Return'][i-1])[:-1])/100
#	print(rf)
	
	a_num = 0
	b_num = 0
	a_sum = 0.0
	b_sum = 0.0

	rf = pd.DataFrame.median(df[col])


	for x in df[col]:
		if x >= rf:
			a_sum += x-rf
			a_num += 1
		else:
			b_sum += rf-x
			b_num += 1

	names.append(col)
	omega.append((a_sum/a_num)/(b_sum/b_num))

result = pd.DataFrame({'ETF': names, 'Omega': omega})
#result = result.sort_values(by=['Omega'])
result = result.reset_index(drop=True);
print(result)

#result.to_csv('Omega_weekly.csv', index=False)
