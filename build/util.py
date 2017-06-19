# imports - standard imports
import os
import re

def pardir(path, up = 1):
    for i in range(up):
        path = os.path.dirname(path)

    return path

def relurljoin(*args):
    construct = '/'.join([s for s in args])
    sanitized = re.sub('/+', '/', construct)

    return sanitized
