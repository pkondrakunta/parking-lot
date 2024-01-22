from application import app

@app.route("/")
@app.route("/index")
def home():
    return "<h1>Welcome to Parkify, hello there!</h1>"