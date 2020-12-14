from flask import Flask,request, redirect, url_for, abort
from flask import render_template
import importdata as d
import json
app = Flask(__name__)



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/aboutapi')
def api_detail():
    return render_template('aboutapi.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/result')
def result():
    return render_template('result.html')

tmpli = []
#사용자로부터 입력한 동네 읽어오는 거임 get방식으로
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method=='POST':
        pass
    elif request.method=='GET':
        temp=request.args.get('get-name')
        tmpli = temp.split(",")

        new_list = []
        for v in tmpli:
            if v not in new_list:
                new_list.append(v)

        name_li = []
        score_li = []
        score = 0
        for i in new_list:
            name_li.append(i)
            if (d.data1(i) == -1):
                score_li.append(d.data2(i))
            elif(d.data2(i) == -1):
                score_li.append(d.data1(i))
            else:
                score_li.append((d.data1(i) + d.data2(i)) / 2)
        tu = list(zip(name_li, score_li))

        tu.sort(key=lambda x:x[1], reverse=True)
        dic = {"meta" : {"total_count" : len(score_li)}, "AreaDocument" : []}


        for i in range(len(score_li)):
            tmp_dic = {}
            tmp_dic["동이름"] = tu[i][0]
            tmp_dic["순위"] = i+1
            tmp_dic["점수"] = tu[i][1]
            dic["AreaDocument"].append(tmp_dic)
        with open('final/SOC/serviceSystem/jfile_.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        with open('final/SOC/serviceSystem/jfile_.json', 'r', encoding='utf-8') as f:
            sample = json.load(f)
        print(sample)
        return render_template('result.html',total_count=len(score_li),tu=tu,sample=sample)
    #arr=request.form.get('demo-name')
    # print(arr)
    # return arr

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(host = "0.0.0.0")#host = "0.0.0.0"