# fintech-hw4-group14

步驟
---
`1、 從Yahoo finance中爬蟲出最近三年的39种ETF的adj close 和return的資料。`
----

数据来源：Yahoo finance 网站（https://finance.yahoo.com/quote/VNQ/performance?p=VNQ&.tsrc=fin-srch）

得到最近三年的月资料、周资料和return資料。(見monthly.csv 、weekly.csv和 returns.csv)

![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/monthly.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/weekly.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/return%20.png)



`2、 觀察我們得到的數據的分佈情況。`
---
畫出各月ETF的直方圖
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/hisrogram%E5%9C%96%E7%89%87.png)
畫出每個月ETF收盤價的的分布圖
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/pdf%E5%88%86%E5%B8%83%E5%9C%96.png)


`3、 根據paper中的，再根據三個指標進行排序。`
---
 `#月資料分析組 `

omega 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/omega-ranking.png)
---

riskness 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/riskness-ranking.png)
---

sharp ratio ASKSR 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/ASKSR-ranking.png)
---

`#周資料分析組 ` 

omega 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/omega-weekly.png)
---

riskness 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/riskness-week.png)
---

sharp ratio ASKSR 評比指標
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/sharp%EF%BC%8Dweekly.png)
---

`4、週資料或月資料結果評比相似嗎?`
----
大致相似，omega 指標評比出來的ETF 的月和周的順序是一致。riskness 和sharpASKSR 的月和周的ETF 排名大概是一樣的。
---
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/omega%20month%20%E4%B8%8Eweek%20%E5%B0%8D%E6%AF%94.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/riskniss%20month%E5%92%8Cweek%E5%B0%8D%E6%AF%94.png)
![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/sharp%20ASKSR-month%20week%20%E5%B0%8D%E6%AF%94.png)

`5、不同指標評比結果相似嗎?`
---

由下圖可以看出不相似，omega和其他兩個指標，非常不相似，但是riskness 和 sharp ASKSR 的ETF 排名比較相似。
---
下圖分別為，在月資料和周資料的兩種情況下的情況。
---

![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/%E6%9C%88%E8%B3%87%E6%96%99%E4%B8%8B%E4%B8%89%E5%80%8B%E6%8C%87%E6%A8%99%20.png)

![Alt text](https://github.com/gongfangntu/fintech-hw4/blob/master/images/%E5%91%A8%E8%B3%87%E6%96%99%E4%B8%8B%E4%B8%89%E5%80%8B%E6%8C%87%E6%A8%99%E6%8E%92%E5%90%8D.png)
