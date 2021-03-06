from flask import Flask, render_template, request, redirect # 追加で2つimportする
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)


# @app.route('/')  # GETメソッドしか受け取れない
@app.route('/', methods=["GET", "POST"])  # GETとPOSTを受け取れる
def index():
    return render_template("index.html")


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
