from flask import Flask

# この場合 __name__ は hello になる
# print(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
