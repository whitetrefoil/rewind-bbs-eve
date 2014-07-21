# !/usr/bin/env python


"""Module utils.auth.b_auth: The basic auth.

Will be used for requesting token.
"""


from eve.auth import BasicAuth
from werkzeug.security import check_password_hash
# I don't know why `import app from app` will cause a crash...
import app


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


class BAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        try:
            accounts = app.app.data.driver.db['accounts']
            account = accounts.find_one({'username': username})
            return check_password_hash(pwhash=account['password'],
                                       password=password)
        except:
            return False


if __name__ == '__main__':
    pass
