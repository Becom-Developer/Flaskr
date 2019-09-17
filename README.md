# NAME

Flaskr - flask フレームワーク学習用

# SYNOPSIS

## SETUP

### python3

Mac でのインストールの場合

公式サイトのダウンロードからインストール

今回は 3.7.4 を選択

参考記事 - <https://docs.python.org/ja/3/using/mac.html>

```
(インストールされたことの確認)
$ which python3.7
/usr/local/bin/python3.7
```

### venv

venv を使った実行方法ですすめる

```
(プロジェクトのディレクトリへ)
$ cd ~/github/Flaskr
$ python3.7 -m venv venv

(有効化)
$ source ~/github/Flaskr/venv/bin/activate

$ cd ~/github/Flaskr
$ python3.7 -m venv venv
$ source ~/github/Flaskr/venv/bin/activate

(有効化された)
(venv) $

(終了するときは無効化)
(env) $ deactivate
```

### pip

拡張ライブラリーをインストールするために pip を使う

インストールしたいプロジェクトのディレクトリへ移動している前提にて

```
(pip コマンドの確認)
$ which pip3.7
/usr/local/bin/pip3.7

(インストールしたいプロジェクトへ移動してインストール実行)
$ cd ~/github/Flaskr
$ source ~/github/Flaskr/venv/bin/activate

(pip コマンドアップグレード)
(venv) $ pip3.7 install pip --upgrade

(インストール)
(venv) $ pip3.7 install Flask

(インストール後は履歴を取っておく)
(venv) $ pip3.7 freeze >> requirements.txt
```

すでに requirements.txt が存在する場合のインストール

```
(venv) $ pip3.7 install -r requirements.txt
```

### git

gitignore がない場合は作成する

```
$ echo 'venv/' >> .gitignore; echo '*.pyc' >> .gitignore; echo '__pycache__/' >> .gitignore; echo 'instance/' >> .gitignore; echo '.pytest_cache/' >> .gitignore; echo '.coverage' >> .gitignore; echo 'htmlcov/' >> .gitignore; echo 'dist/' >> .gitignore; echo 'build/' >> .gitignore; echo '*.egg-info/' >> .gitignore;
```

もしくは

```
$ cat >> .gitignore << 'EOF'
venv/
*.pyc
__pycache__/
instance/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
EOF
```

# TODO

tutorial_01.md

# SEE ALSO

<https://docs.python.org/3/contents.html> - Pythonドキュメント
<https://flask.palletsprojects.com/en/1.1.x/> - Flask
