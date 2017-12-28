from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ran')
def ran():
    return 'Ran Hongmin'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/user/age/<int:user_age>')
def show_user_age(user_age):
    return 'User %d' % user_age


# @app.route('/user/age/<int:user_age>')
# def show_user_age(user_age):
#     return 'User %d' % user_age

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login'
        print("login")
    else:
        return 'no login'
        print ("no Login")


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'about'


if __name__ == '__main__':
    app.run()
