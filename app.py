from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is an about me page"

if __name__ == '__main__':
    app.run(debug=True)