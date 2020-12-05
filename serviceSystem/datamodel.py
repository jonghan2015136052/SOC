def normalization(x):
    min_value = min(x)
    max_value = max(x)

    return list(map(lambda x: (x-min_value)/(max_value-min_value) *10, x))


import csv
import pandas as pd
from pandas import DataFrame
from pandas import Series
# import numpy as np
import json

sub = pd.read_csv('c:\\data2.csv', encoding='cp949')
group = sub.filter(['법정동명', '공시지가(원/㎡)'])
result = group.groupby(['법정동명'])['공시지가(원/㎡)'].mean()
dic = result.to_dict()

a = list(dic.keys())
b = list(dic.values())

c = normalization(b)
for i, j in zip(a, c):
    dic[i] = j
i = 1
for key, val in dic.items():
    print(i, key, " >>> 점수 : ", val)
    i = i + 1
import operator

sub = pd.read_csv('c:\\data.csv', encoding='cp949')
group = sub.filter(['행정구역', '2020년09월_총인구수'])
result = group.groupby(['행정구역'])['2020년09월_총인구수'].sum()
dic = result.to_dict()
dic2 = {}
# print(dic)
for key, val in dic.items():
    if ("서울" in key):
        dic2[key] = val

a = list(dic2.keys())

b = []
for i in dic2.values():
    b.append(int(i.replace(',', "")))

c = normalization(b)

for i, j in zip(a, c):
    dic2[i] = j

i = 1
for key, val in dic2.items():
    print(i, key, " >>> 점수 : ", val)
    i = i + 1
i = 1



# 오름차순 출력
# sdict = sorted(dic2.items(), key=operator.itemgetter(1))
# for key, val in sdict:
#    print(i, key," >>> 점수 : " ,val)
#    i = i + 1
