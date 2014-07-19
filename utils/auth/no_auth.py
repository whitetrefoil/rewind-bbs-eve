# !/usr/bin/env python


"""Module utils.auth.NoAuth: Fake auth, for development to use."""


from eve.auth import BasicAuth


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


class NoAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return True


if __name__ == '__main__':
    pass
