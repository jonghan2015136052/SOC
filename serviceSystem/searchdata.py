import pymysql.cursors
mydb = pymysql.connect(
    user='root',
    passwd='0515',
    db='socdb',
    charset='utf8'
)
cursor = mydb.cursor()
#sdad
#sql = """select *from landprice(idx, name, price)"""
i = 1

sql = "select *from landprice"
cursor.execute(sql)
dic = cursor.fetchall()
sql = "select *from population"
cursor.execute(sql)
dic2 = cursor.fetchall()
mydb.commit()
mydb.close()
def data1(input):
    score = 0
    j = 1
    for i in dic:
        if(input in i[1]):
            score += float(i[2])
            j+=1
    score /= j
    return score

def data2(input):
    score = 0
    j = 1
    for i in dic2:
        if (input in i[1]):
            score += float(i[2])
            j+=1
    score /= j
    return score