from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create")
def createTicket():
    return render_template("createTicket.html")

@app.route("/pay")
def payForTicket():
    return render_template("payTicket.html")

