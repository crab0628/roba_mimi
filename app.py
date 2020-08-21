# FlaskからimportしてFlaskを使えるようにする
import sqlite3, os
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
# appという名でアプリを作る宣言
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'robamimi'


# ページ移動用ルーティング（ここから）
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/in")
def in_html():
    return render_template("in.html")

# @app.route("/check")
# def check_html():
#     return render_template("check.html")

@app.route("/hole")
def hole_html():
    return render_template("hole.html")

@app.route("/out")
def out_html():
    return render_template("out.html")
# ページ移動用ルーティング（ここまで）

# コメント送信、登録機能
@app.route('/check', methods=["POST"])
def add_comment():
    conn = sqlite3.connect("")
    # 課題2の答えはここ 現在時刻を取得
    # time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # POSTアクセスならDBに登録する
    # フォームから入力されたアイテム名の取得(Python2ならrequest.form.getを使う)
    comment = request.form.get("comment")
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    # 現在の最大ID取得(fetchoneの戻り値はタプル)

    # 課題1の答えはここ null,?,?,0の0はdel_flagのデフォルト値
    # 課題2の答えはここ timeを新たにinsert
    c.execute("insert into bbs values(null,?,?)", (comment, icon_id))
    conn.commit()
    conn.close()
    return redirect('/hole')






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