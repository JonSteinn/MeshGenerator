from flask import Flask
from flask import render_template

app = Flask(__name__)

from py_scripts import functions

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
