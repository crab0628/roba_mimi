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

# check 表示
@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' in session :
        conn = sqlite3.connect('service.db')
        c = conn.cursor()
        c.execute("select comment from bbs where id = ?", (id,) )
        comment = c.fetchone()
        conn.close()

        if comment is not None:
            # None に対しては インデクス指定できないので None 判定した後にインデックスを指定
            comment = comment[0]
            # "りんご" ○   ("りんご",) ☓
            # fetchone()で取り出したtupleに 0 を指定することで テキストだけをとりだす
        else:
            return "アイテムがありません" # 指定したIDの name がなければときの対処

        item = { "id":id, "comment":comment }

        return render_template("edit.html", comment=item)
    else:
        return redirect("/login")


# /add ではPOSTを使ったので /edit ではあえてGETを使う
@app.route("/edit")
def update_item():
    if 'user_id' in session :
        # ブラウザから送られてきたデータを取得
        item_id = request.args.get("item_id") # id
        item_id = int(item_id)# ブラウザから送られてきたのは文字列なので整数に変換する
        comment = request.args.get("comment") # 編集されたテキストを取得する

        # 既にあるデータベースのデータを送られてきたデータに更新
        conn = sqlite3.connect('service.db')
        c = conn.cursor()
        c.execute("update bbs set comment = ? where id = ?",(comment,item_id))
        conn.commit()
        conn.close()

        # アイテム一覧へリダイレクトさせる
        return redirect("/bbs")
    else:
        return redirect("/login")


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