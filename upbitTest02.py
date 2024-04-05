import requests
import pyupbit      # 파이썬 용 upbit api 라이브러리


coinTicker = pyupbit.get_tickers(fiat="KRW")


print(coinTicker)


url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

print(res.json())
