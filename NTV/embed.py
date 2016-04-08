#! /usr/bin/env python
import os
import sys
import NTV

if sys.platform == 'darwin':
    plug_loc = os.path.expanduser('~/Library/Application Support/NTV')
elif sys.platform == 'win32':
    plug_loc = os.path.join(environ['APPDATA'], 'NTV')
else:
    plug_loc = os.path.expanduser(os.path.join("~", "." + 'NTV'))

plug_loc = os.path.join(plug_loc,'plugins')
sys.path = [plug_loc] + sys.path
try:
    from python_embed.python_embed import *
except:
    from .plugins.python_embed.python_embed import *
