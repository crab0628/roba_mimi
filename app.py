# FlaskからimportしてFlaskを使えるようにする
import sqlite3, os, psycopg2 
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
# import pandas as pd
# appという名でアプリを作る宣言
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'robamimi'

# connect postgreSQL
# users = 'gwcelufhgolnrq' # initial user
# dbnames = 'dao2p7dtg0lftj'
# passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
# host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
# port = '5432'
# sslmode = 'require'
# conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   


# ページ移動用ルーティング（ここから）
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/in")
def in_html():
    return render_template("in.html")

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
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect("roba_mimi.db")
    comment = request.form.get("comment")
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect('roba_mimi.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbs VALUES (default,'" + comment + "' , null)")
    conn.commit()
    conn.close()
    return redirect('/bbs')

# bbs コメント表示
@app.route('/bbs')
def bbs():
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect('roba_mimi.db')
    c = conn.cursor()
    c.execute("select id,comment from bbs where id = (select max(id) from bbs) and flag is null")
    comment_new = c.fetchone()
    # 最新コメント↑、それ以外↓
    c.execute("select id,comment from bbs where flag is null order by random()")
    comment_list = []
    for row in c.fetchall():
        comment_list.append({"id": row[0], "comment": row[1]})

    c.close()
    return render_template('bbs.html' , comment_list = comment_list , comment_new = comment_new)

@app.route('/check')
def check():
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect('roba_mimi.db')
    c = conn.cursor()
    c.execute("select max(id),comment from bbs where flag != 1 group by id")
    comment_new = c.fetchone()
    c.execute("select id,comment from (select * from bbs where flag is null order by id desc limit 50) as A order by random() limit 20")
    comment_list = []
    for row in c.fetchall():
        comment_list.append({"id": row[0], "comment": row[1]})

    c.close()
    return render_template('check.html' , comment_list = comment_list , comment_new = comment_new)

@app.route('/del' ,methods=["POST"])
def del_task():
    # クッキーから user_id を取得
    id = request.form.get("comment_id")
    # id = int(id)
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect("roba_mimi.db")
    c = conn.cursor()
    c.execute("update bbs set flag = 1 where id = '" + id + "'")
    conn.commit()
    c.close()
    return redirect("/check")

@app.route('/del2' ,methods=["POST"])
def del_bbs():
    # クッキーから user_id を取得
    id = request.form.get("comment_id")
    # id = int(id)
    users = 'gwcelufhgolnrq' # initial user
    dbnames = 'dao2p7dtg0lftj'
    passwords = '67ae8e69b0ee835b3819a947d0aec3818072a62ce959b57e02d92a35eb34c0d7'
    host = 'ec2-54-86-57-171.compute-1.amazonaws.com'
    port = '5432'
    sslmode = 'require'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords +" host=" + host + " port=" + port)   
    # conn = sqlite3.connect("roba_mimi.db")
    c = conn.cursor()
    c.execute("update bbs set flag = 1 where id = id", (id,))
    conn.commit()
    c.close()
    return redirect("/in")







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


# ↓ 制作、更新時の切り替え忘れない！

if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     app.run(debug=True)