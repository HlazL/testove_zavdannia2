import hashlib
from sqlalchemy import func
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = hashlib.sha1( 'abcdefg'.encode() ).hexdigest()

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db/users.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import *

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        name = request.form.get('name')
        user = Users.query.filter_by(name=name).first()
        if not (name and name.strip()):
            flash("Будь ласка, вкажи ім'я")
            return render_template("index.html")
        if user:
            return render_template("hello_again.html", name=request.form.get("name"))

        else:
            # create a new user with the form data
            name = func.lower(name)
            new_user = Users(name=name)
            # add the new user to the DB
            db.session.add(new_user)
            db.session.commit()

            return render_template("hello.html", name=request.form.get("name"))

@app.route("/users")
def users():
    users = Users.query.all()
    return render_template("users.html", users=users)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
