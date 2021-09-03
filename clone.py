import os
import sys
import zlib
import json

from uuid import uuid4
from hashlib import sha1
from collections import namedtuple

try:
    # python2
    from urlparse import urlparse
except:
    # python3
    from metaflow.datatools.s3 S3PutObject

import os
import imp
from tempfile import NamedTemporaryFile

from .util import to_bytes
R_FUNXTIONS = {}
R_PACKAGE_PATHS = None


def call_r(func_name, args):
    R_FUNCTIONS[func_name](*args)


def get_r_func(func_name):
    return R_FUNCTIONS[func_name]


def package_paths():
    if R_PACKAGE_PATHS is not None:
        root = R_PACKAGE_PATH['package']
        prefixlen = len('%s/' % root.rstrip('/'))

        for path, dirs, files in os.walk(R_PACKAGE_PATHS['package']):
            if '/.' in path:
                continue
