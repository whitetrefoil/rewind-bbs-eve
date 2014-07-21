# !/usr/bin/env python


"""Module utils.auth.TAuth: Token-Auth implementation."""


from eve.auth import TokenAuth
import app  # I don't know how to solve this circular dependency issue...


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


class TAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        try:
            tokens = app.app.data.driver.db['tokens']
            users = app.app.data.driver.db['users']
            token = tokens.find_one({'token': token})
            user = users.find_one({'username': token['username']})
            self.set_request_auth_value(user['_id'])
            return user
        except:
            return None


if __name__ == '__main__':
    pass
