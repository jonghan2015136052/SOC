import json

with open('data1.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)
with open('data2.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)
li1 = []
li2 = []
li3 = []
li4 = []
for i in data1:
    li1.append(i["name"])
for i in data1:
    li2.append(i["price"])

for i in data2:
    li3.append(i["name"])
for i in data2:
    li4.append(i["population"])

def data1(input):
    score = 0
    j = 0
    for i in list(zip(li1, li2)):
        if(input in i[0]):
            score += 10 - float(i[1])
            j+=1
    if(j !=0):
        score /= j
        return score
    elif(j == 0):
        return -1


def data2(input):
    score = 0
    j = 0
    for i in list(zip(li3, li4)):
        if (input in i[0]):
            score += float(i[1])
            print(score)
            j+=1
    if (j != 0):
        score /= j
        return score
    elif (j == 0):
        return -1
