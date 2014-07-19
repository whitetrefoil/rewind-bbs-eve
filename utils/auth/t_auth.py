# !/usr/bin/env python


"""Module utils.auth.TAuth: Token-Auth implementation."""


from eve.auth import BasicAuth


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


class TAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        users = app.data.driver.db['users']
        tokens = app.data.driver.db['tokens']


if __name__ == '__main__':
    pass
