# !/usr/bin/env python


"""rewind_bbs.py: The main entry file of this application"""


from app import app
import callbacks


__author__ = "WhiteTrefoil"
__credits__ = ["WhiteTrefoil"]
__version__ = "0.0.0"
__maintainer__ = "WhiteTrefoil"
__email__ = "whitetrefoil@gmail.com"
__status__ = "Prototype"


app.debug = True

# Events
app.on_insert_tokens += callbacks.token.generate_token
app.on_post_POST_tokens += callbacks.token.respond_token


if __name__ == '__main__':
    app.run()
