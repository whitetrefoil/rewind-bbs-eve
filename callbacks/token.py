# !/usr/bin/env python


"""Module events.token: Some hacks to implement the custom token auth."""


import json
from flask import request
from uuid import uuid4
from app import app


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


def generate_token(items):
    username = request.authorization['username']
    tokens = app.data.driver.db['tokens']
    tokens.remove({'username': username})
    items[0]['token'] = str(uuid4())
    items[0]['username'] = request.authorization['username']


def respond_token(req, res):
    orig = json.loads(res.data.decode())
    exports = {
        'username': orig['username'],
        'token': orig['token']
    }
    res.data = bytes(json.dumps(exports), 'utf-8')


if __name__ == '__main__':
    pass
