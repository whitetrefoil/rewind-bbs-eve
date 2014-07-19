# !/usr/bin/env python


"""settings.py: The settings file of Eve"""


import models


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


# API Config
ALLOWED_FILTERS = []
SORTING = False
PAGINATION = True
ITEM_LOOKUP = True  # TODO
PROJECTION = False
BANDWIDTH_SAVER = False  # TODO

DOMAIN = {
    'posts': models.post,
    'comments': models.comment,
    'tokens': models.token
}

# DB Config
MONGO_HOST = 'localhost'
MONGO_DBNAME = 'rewind-bbs-eve'
# ID_FIELD = 'id'
# LAST_UPDATED = 'updated'
# DATE_CREATED = 'created'

# Resource Config
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']


if __name__ == '__main__':
    pass
