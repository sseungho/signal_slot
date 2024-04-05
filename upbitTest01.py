import requests
import json
import time

while True:

    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    response = requests.get(url)
    # print(response.text)

    responseJson = response.json()  # Json 함수로 리스트 타입 변경
    # print(responseJson)

    print(responseJson[0]['trade_price'])
    time.sleep(2)



