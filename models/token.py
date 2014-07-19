# !/usr/bin/env python


"""Module models.token: The model of "Token"."""


from schemata.token import schema
from utils.auth import BAuth


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


token = {
    'url': 'login',
    'datasource': {
        'source': 'tokens'
    },
    'resource_methods': ['POST'],
    'item_methods': [],
    'item_lookup': False,
    'authentication': BAuth(),
    'schema': schema
}


if __name__ == '__main__':
    pass
