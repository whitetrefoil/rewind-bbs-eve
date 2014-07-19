# !/usr/bin/env python


"""Module utils.auth.b_auth: The basic auth.

Will be used for requesting token.
"""


from eve.auth import BasicAuth


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


class BAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'username' and password == 'password'


if __name__ == '__main__':
    pass
