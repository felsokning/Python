#!/usr/bin/env python
"""Modifies the SRT (SubRip Text) files found in the path, to contain the appropriate language code.

    Some tools, such as svtplay-dl, download SRT files for videos but do not stamp the appropriate language on
    the SRT file. This causes problems when you then import them into a media library manager (e.g.: Plex). Until
    this can be addressed in those tools, this script aims to modify the SRT file names, so that it
    needn't be done manually.

REQUIREMENTS:
    None

TO RUN:
    python3 RenameSrtFiles.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import os

# Modify path to where the SRT files are dropped.
path = "*"
language_code = "*"
files = os.listdir(path)
srt_files = list()
for f in files:
    if f.__contains__("srt") and not f.__contains__(language_code):
        srt_files.append(f)

for srt in srt_files:
    srt_strings = srt.rsplit(".", 1)
    new_srt_name = srt_strings[0] + "." + language_code + "." + srt_strings[1]
    source = path + "/" + srt
    destination = path + "/" + new_srt_name
    os.rename(source, destination)
