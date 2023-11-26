from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def f(celsius=0.0):
    """Convert celsius to fahrenheit"""

    f = float(celsius) * 9.0 / 5 + 32

    return f'{celsius} celsius is {str(f)} F'


if __name__ == '__main__':
    app.run()
