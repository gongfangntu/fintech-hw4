# fintech-hw4-group14
==
步驟
---
1、 從Yahoo finance中爬蟲出最近三年的39种ETF的adj close 和return的資料。
----

数据来源：Yahoo finance 网站（https://finance.yahoo.com/quote/VNQ/performance?p=VNQ&.tsrc=fin-srch）

得到最近三年的月资料、周资料和return資料。(見monthly.csv 、weekly.csv和 returns.csv)

![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/monthly.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/weekly.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/return%20.png)

参考程式见

2、 用omega 指標來計算。
---
畫出各月ETF的直方圖
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/hisrogram%E5%9C%96%E7%89%87.png)
畫出每個月ETF收盤價的的分布圖
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/pdf%E5%88%86%E5%B8%83%E5%9C%96.png)

根據paper中的公式來算出omega的值，再根據指標進行排序。


