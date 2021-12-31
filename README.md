# Flask練習

Flaskを使ってREST APIを作るための練習をする。


## 環境構築
```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pytest flask gunicorn
```

## 実行方法
hello.pyのappを実行するには以下の2種類の方法がある。
appはFlask(__name__)として、定義している。

```
# Flask内の開発用サーバーソフトで実行する場合。
FLASK_APP=hello FLASK_ENV=development flask run

# 本番環境向けにGunicornというサーバーソフトで実行する場合
gunicorn hello:app
```
