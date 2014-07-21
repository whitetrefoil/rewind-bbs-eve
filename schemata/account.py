# !/usr/bin/env python


"""Module schemata.account: The schema of "Account".

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
        'data_relation': {
            'resource': 'users',
            'field': 'username',
            'embeddable': False
        }
        # Won't set this to unique
        # Will implement "unique" in the API logic
    },
    'password': {
        'type': 'string',
        'required': True
    }
}


if __name__ == '__main__':
    pass
