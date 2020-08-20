# FlaskからimportしてFlaskを使えるようにする
import sqlite3, os
from flask import Flask, render_template, request, session, redirect, url_for
# appという名でアプリを作る宣言
app = Flask(__name__)


# ページ移動用ルーティング（ここから）
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/in")
def in_html():
    return render_template("in.html")

@app.route("/check")
def check_html():
    return render_template("check.html")

@app.route("/hole")
def hole_html():
    return render_template("hole.html")

@app.route("/out")
def out_html():
    return render_template("out.html")
# ページ移動用ルーティング（ここまで）







# css読み込み用コード
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



if __name__ == "__main__":
    app.run(debug=True)