from flask import Flask

app = Flask(__name__)


@app.route("/<int:numero>", methods=['GET', 'POST'])
def hello(numero: int):
    return f"ola mundo, {numero}"


if __name__ == "__main__":
    app.run(debug=True)
