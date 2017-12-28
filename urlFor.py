from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index(): pass


# @app.route('/login')
# def login(): pass


@app.route('/user/<username>')
def profile(username): pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("login")
    else:
        print ("no Login")


with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='Ran Hongmin')
