from flask import Flask,request, redirect, url_for, abort
from flask import render_template
import importdata as d
import json

app = Flask(__name__)



@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def htest():
    return render_template('test.html')

@app.route('/landing')
def hello_world3():
    return render_template('landing.html')

@app.route('/generic')
def hello_world4():
    return render_template('generic.html')


@app.route('/result')
def hello_world5():
    return render_template('result.html')

tmpli = []
#사용자로부터 입력한 동네 읽어오는 거임 get방식으로
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method=='POST':
        pass
    elif request.method=='GET':
        temp=request.args.get('demo-name')
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
        with open("jfile.json", "w", encoding = 'utf-8') as f:
            json.dump(dic, f)
        with open('jfile.json', 'r', encoding = 'utf-8') as f:
            sample = json.load(f)
        print(sample)
        return render_template('result.html',total_count=len(score_li),tu=tu)
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
    app.run()#host = "0.0.0.0"