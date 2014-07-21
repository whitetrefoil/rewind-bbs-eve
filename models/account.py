# !/usr/bin/env python


"""Module models.account: The model of "Account".

This model will be exported as "resetpassword".
"""


from schemata.account import schema


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


account = {
    'url': 'resetpassword',
    'datasource': {
        'source': 'accounts'
    },
    'hateoas': False,
    'resource_methods': ['POST'],
    'item_methods': [],
    'item_lookup': False,
    'schema': schema
}


if __name__ == '__main__':
    pass
