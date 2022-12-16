## 抓取台灣證券交易所資料
## 用post方法，從network取得payload的form data

import requests
import pandas as pd

url = "https://www.twse.com.tw/zh/exchangeReport/MI_INDEX"

payload = {'response':'csv',
           'date':'20221215',
           'type': 'ALLBUT0999'}

resp = requests.post(url, data=payload)

if resp.status_code==200:
    with open('台灣證券1215.csv', 'w', encoding="utf-8-sig") as fobj:
        fobj.write(resp.text)
        #print(resp.text)