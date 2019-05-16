#爬蟲用的library
from pandas_datareader import data as web
import fix_yahoo_finance as yf

#資料處理的library
import pandas as pd
import datetime as dt
import time
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

#讀取老師給的CSV檔
df = pd.read_csv('Real Estate ETF List (48).csv', encoding = 'UTF-8')


# 抓取 2016-01-01 之前成立的公司
df['Inception'] = df['Inception'].astype(str)
df['Inception'] = [time.strptime(date, "%d/%m/%Y") for date in df['Inception']]
df = df[df.Inception <= time.strptime('01/01/2016', "%d/%m/%Y")]
df = df.reset_index(drop=True);

#print(df)

# 將每個ETF的縮寫抓出
name = df['Symbol']
#print(name)

name.to_csv('return.csv')
print(name)

'''
yf.pdr_override()

# 時間開始和結束點(從now()往回推3年)
start = datetime.now() - relativedelta(years=3)
end = datetime.now()

print(start)
print(end)

#爬蟲部分(週資料)
for i in range(len(name)):
	df = web.get_data_yahoo([name[i]],start, end, interval='1mo') 
	df = df.reset_index()
	if name[i] == 'WREI':
		print(df)
	df.drop(df[df['Adj Close'].isnull()].index, inplace=True)
	df = df.reset_index(drop=True);
	#print(df['Adj Close'])
	if(name[i] == 'WREI'):
		print(df)
	
	
#	df['Date'] = df['Date'].astype(str)


	#第一個Column為時間
	if i == 0:	
		dict_new = {
			"Date": df["Date"]
		}
		df_new = pd.DataFrame(dict_new)
	
	
	#後面的column為每個ETF的收盤價
	df_new[name[i]] = df['Adj Close']

#print(df_new)

#轉成CSV檔

df_new = df_new.set_index('Date')
print(df_new)

df_new.to_csv('weekly.csv')

'''
