from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Docker!</h1>"

@app.route("/about")
def about():
    return "Docker Training Project"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
