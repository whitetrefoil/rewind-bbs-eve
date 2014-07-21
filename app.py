# !/usr/bin/env python


"""app.py: This file will declare the app instance.

(in order to share it among modules)
"""


from eve import Eve
from utils.auth.t_auth import TAuth


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


app = Eve(auth=TAuth)


if __name__ == '__main__':
    pass
