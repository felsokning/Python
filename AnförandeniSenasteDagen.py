#!/usr/bin/env python
"""Checks if there have been any speeches published at the Riksdagen in the last day.

Uses Requests (https://docs.python-requests.org/en/master/) to see if the Riksdagen () has published any speeches in
the last day and, if so, what they were. (Spoiler alert: You can open hyperlinks from terminal.)

REQUIREMENTS:
    requests

TO RUN:
    python3 AnförandeniSenasteDagen.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import datetime
import SwedishDate
import requests

# För felsökning i PyCharm (eller python, om du vill att göra det).
if __debug__:
    date = SwedishDate.date.today() - datetime.timedelta(days=2)
else:
    date = SwedishDate.date.today() - datetime.timedelta(days=1)

riksdagen_url = "https://data.riksdagen.se/anforandelista/?rm=&anftyp=Nej&d={0}-{1}-{2}" \
                "&ts={0}-{1}-{2}&parti=&iid=&sz=10&utformat=json".format(date.year, date.month, date.day)
response = requests.get(riksdagen_url)

# Jag tycker om när den svensk gudar är glad.
if response.status_code is 200:
    json_response = response.json()
    count = json_response['anforandelista']['@antal']
    if int(count) > 0:
        print("De hade {} anföranden i senaste dagen.".format(count))
        anföranden = count = json_response['anforandelista']['anforande']
    else:
        print("De hade ingen anföranden igår.")
for anförande in anföranden:
    print("{0}: {1} - {2}".format(anförande["dok_id"], anförande["dok_titel"], anförande["protokoll_url_www"]))
