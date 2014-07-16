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
DOMAIN = {
    'posts': models.post
}

# DB Config
MONGO_HOST = 'localhost'
MONGO_DBNAME = 'rewind-bbs-eve'

# Resource Config
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


if __name__ == '__main__':
    pass
