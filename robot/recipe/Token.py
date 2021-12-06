# encoding:utf-8
import requests 
import json

def access_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=sAg5QeiSNt9fjhPvDGM5Wvpe&client_secret=AW59xmqutj5kmF00YPrSiqGHyUUB8AG7'
    response = requests.get(host)
    if response:
        token_content = response.json()
        token = token_content['access_token']
        return token