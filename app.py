# FlaskからimportしてFlaskを使えるようにする
import sqlite3
from flask import Flask, render_template, request, session, redirect
# appという名でアプリを作る宣言
app = Flask(__name__)

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





if __name__ == "__main__":
    app.run(debug=True)