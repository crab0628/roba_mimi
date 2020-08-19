# FlaskからimportしてFlaskを使えるようにする
import sqlite3
from flask import Flask, render_template, request, session, redirect
# appという名でアプリを作る宣言
app = Flask(__name__)




if __name__ == "__main__":
    app.run(debug=True)