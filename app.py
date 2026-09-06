from flask import Flask, request
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)

    return f"""
    <html>
    <head>
        <title>Calculator</title>
    </head>

    <body>

        <h1>Calculator Application</h1>

        <form method="POST">

            <label>First Number:</label>
            <input type="number" step="any" name="a" required>

            <br><br>

            <label>Second Number:</label>
            <input type="number" step="any" name="b" required>

            <br><br>

            <button type="submit" name="operation" value="add">
                Add
            </button>

            <button type="submit" name="operation" value="subtract">
                Subtract
            </button>

            <button type="submit" name="operation" value="multiply">
                Multiply
            </button>

            <button type="submit" name="operation" value="divide">
                Divide
            </button>

        </form>

        <br>

        <h2>Result: {result}</h2>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)