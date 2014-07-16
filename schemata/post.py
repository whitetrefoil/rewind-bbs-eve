# !/usr/bin/env python


"""Module schemata.post: The schema of "Post".

Usage: from schemata.post import schema
"""


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


schema = {
    'subject': {
        'type': 'string',
        'minlength': 1,
        'required': True
    },
    'content': {
        'type': 'string',
        'minlength': 1,
        'required': True
    }
}


if __name__ == '__main__':
    pass
