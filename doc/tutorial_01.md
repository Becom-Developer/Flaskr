# NAME

tutorial_01.md - flask チュートリアル (アプリの全体像)

# SYNOPSIS

どういうものを作成するかアプリの概要を決める

`簡易的なログイン機能があるブログシステム`

実装を開始するまえにアプリの全体像を把握しておく

```
flaskr_project
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

ルーティングを考える

- GET - `/hello` -  テスト表示
- GET - `/` -  ブログの一覧表示
- GET - `/create` -  ブログの新規作成画面
- POST - `/create` -  ブログの新規作成登録
- GET - `/:id/update` -  ブログの更新画面
- POST - `/:id/update` -  ブログの更新実行
- POST - `/:id/delete` -  ブログの削除実行
- GET - `/auth/register` -  ユーザー登録画面表示
- POST - `/auth/register` -  ユーザー登録実行
- GET - `/auth/login` -  ログイン画面表示
- POST - `/auth/login` -  ログイン実行
- POST - `/auth/logout` -  ログアウトを実行

起動するスクリプトを用意する

`flaskr_project/hello.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

起動方法 (venv 環境で動作している前提)

```
$ export FLASK_APP=hello.py && flask run
(終了は control + c)
```

これでも起動はするが WARNING 警告が出るので実行モードを指定する

```
$ export FLASK_APP=hello.py && export FLASK_ENV=development && flask run
```

メンテナンスの向上のためにディレクトリ構造を変更する

```
$ mkdir flaskr
```

`flaskr_project/flaskr/__init__.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

```
(アプリ名を変更)
$ export FLASK_APP=flaskr && export FLASK_ENV=development && flask run
```

ルーティングをアプリの仕様に合わせる

`flaskr_project/flaskr/__init__.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
```

# TODO

# SEE ALSO
