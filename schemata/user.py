# !/usr/bin/env python


"""Module schemata.user: The schema of "User".

The difference between "Account" & "User" is that
"User" for general user information
while "Account" for auth info.
"""


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'title': {
        'type': 'string'
    },
    'bio': {
        'type': 'string'
    }
}


if __name__ == '__main__':
    pass
