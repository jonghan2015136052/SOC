from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/landing')
def hello_world3():
    return render_template('landing.html')
@app.route('/generic')
def hello_world4():
    return render_template('generic.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()