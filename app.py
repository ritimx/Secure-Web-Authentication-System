from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

with get_db() as db:
    db.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )""")

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]

        hashed=generate_password_hash(password)

        db=get_db()
        db.execute("INSERT INTO users(username,email,password) VALUES(?,?,?)",
                   (username,email,hashed))
        db.commit()
        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        db=get_db()
        user=db.execute("SELECT * FROM users WHERE email=?",(email,)).fetchone()

        if user and check_password_hash(user["password"],password):
            session["user"]=user["username"]
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html",user=session["user"])
    return redirect("/login")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")

app.run(debug=True)
