from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'blog index'

@app.route('/create')
def create():
    return 'blog create'

@app.route('/<int:id>/update')
def update(id):
    return 'blog update %d' % id

@app.route('/auth/register')
def register():
    return 'blog register'

@app.route('/auth/login')
def login():
    return 'auth login'
