from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return("This is my homepage")

@app.route("/hello/<name>")
def home(name=None):
    return render_template("index.html", name=name)

@app.route("/info", methods=["POST"])
def retrunSomething():
    return jsonify({'info': "Tou have success submit a request"})

if __name__ == "__main__":
    app.run(debug=True)