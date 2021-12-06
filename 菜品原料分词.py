#encoding=utf-8
import csv
import pandas as pd
import re
import json
# file=r"菜品原料.xlsx"

# data_xls = pd.read_excel(file, index_col=0)
# data_xls.to_csv(file.split(".")[0]+".csv", encoding='utf-8')

file=r"菜品原料.csv"
dict1 = {}

csv_reader=csv.reader(open(file,encoding='utf-8'))
for row in csv_reader:
    temp1=row[1].split(",")
    # print(temp1)
    temp4=[]
    temp5=[]
    temp6=[]
    for temp2 in temp1:
        temp3=re.split(r'(\d+)', temp2) 
        for i in temp3:
            j=i.split(";")
            for k in j:
                  if not k.isdigit() and k!="克":
                     temp4.append(k)
    for i in temp4:
        j=i.split("（")[0].replace("\n","").replace(" ","").replace("。","").replace("约","").replace("()","")
        temp5.append(j)
    
    for i in temp5:
        j=re.split("一|二|三|四|五|六|七|八|九|十|两",i)[0].replace("/","").split(")")[-1].replace("对","").replace("各","").replace("?","")
        if j is not "" and j is not '注：可酌情配料':
            temp6.append(j)
    print(temp6)

    dict1[row[0]] = temp6

filename = "food.json"
f = open(filename,'w',encoding='utf-8')
json.dump(dict1,f,ensure_ascii=False)
#f.write(json.dumps(dict1))
f.close()


