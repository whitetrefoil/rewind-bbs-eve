# !/usr/bin/env python


"""Module callbacks.account: Custom API for (re)set password."""


import json
from app import app
from werkzeug.security import generate_password_hash


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


def set_password(items):
    app.data.driver.db['accounts'].remove({'username': items[0]['username']})
    hashed = generate_password_hash(password=items[0]['password'])
    items[0]['password'] = hashed


def respond_password(req, res):
    orig = json.loads(res.data.decode())
    exports = {
        'username': orig['username'],
        '_status': orig['_status']
    }
    res.data = bytes(json.dumps(exports), 'utf-8')


if __name__ == '__main__':
    pass
