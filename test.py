from Study import *
import json
from flask_api import status
from flask import Flask, request
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


app = Flask(__name__)


@app.route('/')
def greeting():
    return "This is Test API!"


@app.route('/add', methods=['POST'])
def get_add():
    if request.method == 'POST':
        a = request.json['a']
        b = request.json['b']
        c = add(a, b)
        result = json.dumps(c)
    return result, status.HTTP_200_OK, {}
