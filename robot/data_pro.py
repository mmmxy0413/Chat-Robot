import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)

def getMaterial(input):
    exist = False
    json_file = BASE_DIR+'/robot/material.json'
    f = open(json_file,'r',encoding='utf-8')
    dict = json.load(f)
    for d in dict:
        if input == d:
            exist = True
    if exist:
        value = dict[input]
        return(value[0])
    return False

def getInfo(input):
    info = ''
    json_file = BASE_DIR+'/robot/information.json'
    f = open(json_file,'r',encoding='utf-8')
    dicts = json.load(f)
    print(type(dicts))
    for dict in dicts:
        if input in dict:
            info = dicts[dict]
            print(info)
            info = input +'的营养信息如下：能量为' + info['energy'] + 'g,蛋白质为' + info['protein'] +'g,脂肪为'+info['fat']+'g。'
            return info
    return False
