from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test')
def helloTest():
    return "Hello World THIS IS A TEST!"

if __name__ == '__main__':
    app.run()