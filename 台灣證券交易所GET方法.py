## 抓取台灣證券交易所資料
## 用get方法，從Network中的payload -> view source -> 取得 esponse=csv&date=20221214&type=ALLBUT0999資料，將此資料貼在網址後方傳輸get資料

import requests
import pandas as pd

url = "https://www.twse.com.tw/zh/exchangeReport/MI_INDEX?response=csv&date=20221214&type=ALLBUT0999"

resp = requests.get(url)

if resp.status_code==200:
    with open('台灣證券1214.csv', 'w', encoding="utf-8-sig") as fobj:
        fobj.write(resp.text)
        #print(resp.text)
