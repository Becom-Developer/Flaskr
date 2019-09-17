from flask import Flask

# この場合 __name__ は flasker になる
# print(__name__)

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
