
import pandas as pd
from matplotlib import pyplot
series = pd.read_csv('/Users/gongfang/Desktop/fintech/HW4/monthly.csv', encoding='utf8')
#series.plot(style='k.')
#pyplot.show()

for col in series:
    if col == 'Date':
        continue

    series[col]




   import pandas as pd
    from matplotlib import pyplot
    series = pd.read_csv('/Users/gongfang/Desktop/fintech/HW4/monthly.csv', encoding='utf8')
    series.hist()
    pyplot.show()