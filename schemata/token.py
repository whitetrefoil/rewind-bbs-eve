# !/usr/bin/env python


"""Module schemata.token: The schema of "Token"."""


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


schema = {
    'token': {
        'type': 'string',
        'unique': True,
        'readonly': True
    }
}


if __name__ == '__main__':
    pass
