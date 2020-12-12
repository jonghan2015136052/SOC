from flask import Flask,request, redirect, url_for, abort
from flask import render_template
import searchdata as d


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
    return render_templsate('result.html')

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
        score = 0
        li = []
        for i in new_list:
            li.append((d.data1(i) + d.data2(i)) / 2)
        li.sort(reverse=True)
        print(li)
        return (temp)
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

