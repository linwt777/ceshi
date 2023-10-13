# -*-coding：utf-8
# @Aunthor:linweiteng
# Date:2023/10/13 16:48
# @File:PostmanForHttpRequest.py
import requests

url = "https://restapi.amap.com/v3/weather/weatherInfo?key=eabfcb6d68f6d059dbbccf81302821f3&city=110101"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
