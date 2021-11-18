from flask import Flask


def add(a, b):
    return a+b


def same(a, b):
    if a == b:
        return True
    else:
        return False


# app.py
app = Flask(__name__)


@app.route('/')
def greeting():
    return "This is Test API!"
