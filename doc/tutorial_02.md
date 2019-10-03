# NAME

tutorial_02.md - flask チュートリアル (簡易的なルーティング)

# SYNOPSIS

最低限度のルーティングを実装

`デザイン以前にテキストだけの表示をする`

- 対象
    - GET - `/hello` -  テスト表示
    - GET - `/` -  ブログの一覧表示
    - GET - `/create` -  ブログの新規作成画面
    - GET - `/:id/update` -  ブログの更新画面
    - GET - `/auth/register` -  ユーザー登録画面表示
    - GET - `/auth/login` -  ログイン画面表示

`flaskr_project/flaskr/__init__.py`

```python
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
```

# TODO

# SEE ALSO
