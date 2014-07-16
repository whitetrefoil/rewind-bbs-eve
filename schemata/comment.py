# !/usr/bin/env python


"""Module schemata.comment: The schema of "Comment".

Usage: from schemata.comment import schema
"""


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


schema = {
    'post_id': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'posts',
            'field': '_id',
            'embeddable': True
        }
    },
    'content': {
        'type': 'string',
        'minlength': 1,
        'required': True
    }
}


if __name__ == '__main__':
    pass
