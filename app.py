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


# コメント送信、登録機能
@app.route('/add', methods=["POST"])
def add_comment():
    conn = sqlite3.connect("comments.db")
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
    c.execute("insert into comments values(null,?)", (comment,))
    conn.commit()
    conn.close()
    return redirect('/check')

# check コメント表示
@app.route('/bbs')
def bbs():
        conn = sqlite3.connect('roba_mimi.db')
        c = conn.cursor()
        # # DBにアクセスしてログインしているユーザ名と投稿内容を取得する
        # クッキーから取得したuser_idを使用してuserテーブルのnameを取得
        # c.execute("select name from user where id = ?", (user_id,))
        # fetchoneはタプル型
        # user_info = c.fetchone()
        # print(user_info)
        c.execute("select id,comment from bbs")
        comment_list = []
        for row in c.fetchall():
            comment_list.append({"id": row[0], "comment": row[1]})

        c.close()
        return render_template('bbs.html' , comment_list = comment_list)

@app.route('/del' ,methods=["POST"])
def del_task():
    # クッキーから user_id を取得
    id = request.form.get("comment_id")
    id = int(id)
    conn = sqlite3.connect("service.db")
    c = conn.cursor()
    c.execute("update bbs set flag = 1 where id = ?", (id,))
    conn.commit()
    c.close()
    return redirect("/bbs")







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