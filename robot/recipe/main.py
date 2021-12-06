# encoding:utf-8

import requests
import base64
from robot.recipe import Token
import re

'''
菜品识别
'''

def recipe_recognitino(picture):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    # 二进制方式打开图片文件
    f = open(picture, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img,"top_num":1}
    access_token = Token.access_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        content = response.json()
        result = content['result'][0]
        #calorie = result['calorie']
        name = result['name']
        return name

    