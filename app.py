from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return "<h1>Hello, there!</h1>"