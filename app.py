from flask import Flask
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Calculator Application</h1>
    <p>Calculator is running successfully on AWS EC2.</p>
    <p>Available operations:</p>
    <ul>
        <li>/add/10/5</li>
        <li>/subtract/10/5</li>
        <li>/multiply/10/5</li>
        <li>/divide/10/5</li>
    </ul>
    """


@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return str(add(a, b))


@app.route("/subtract/<int:a>/<int:b>")
def subtraction(a, b):
    return str(subtract(a, b))


@app.route("/multiply/<int:a>/<int:b>")
def multiplication(a, b):
    return str(multiply(a, b))


@app.route("/divide/<int:a>/<int:b>")
def division(a, b):
    return str(divide(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)