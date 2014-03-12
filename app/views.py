from flask import *
from app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "fish" and request.form["password"] == "chips":
            session["logged_in"] = True
            return redirect(url_for("secret"))
        else:
            error = "Username or password wrong, dude"
            
    return render_template("login.html", error = error)

@app.route("/secret")
def secret():
    return render_template("secret.html")