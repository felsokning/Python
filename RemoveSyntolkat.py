#!/usr/bin/env python
"""Removes the Syntolkat (https://en.wikipedia.org/wiki/Audio_description) files from a given path.

    Some tools, such as svtplay-dl, download videos listed in library succession. For Swedish sites, this can include
    Syntolkat videos, which might not be of any use or importance to your library. This script hopes to address this
    by removing the files from the folder, leaving the standard files intact.

REQUIREMENTS:
    None

TO RUN:
    python3 RemoveSyntolkat.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import os

# Modify the path where the files are dropped.
path = "*"
files = os.listdir(path)
syntolkat_files = list()
for f in files:
    if f.__contains__("syntolkat"):
        syntolkat_files.append(f)

for s in syntolkat_files:
    delete_path = path + "/" + s
    if os.path.isfile(delete_path):
        os.remove(delete_path)
    else:
        print("{} was not found.".format(delete_path))
