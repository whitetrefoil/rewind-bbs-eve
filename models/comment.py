# !/usr/bin/env python


"""Module models.comment: The model of "Comment"."""


from schemata.comment import schema


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


comment = {
    'url': 'posts/<regex("[a-f0-9]{24}"):post_id>/comments',
    'schema': schema
}


if __name__ == '__main__':
    pass
