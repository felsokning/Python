#!/usr/bin/env python
"""Returns the current week number of the year.

As some countries (e.g.: Sweden) use week numbers for organisation, it's
important to be able to return the given week number in an easily referenced
code-base. One could use http://vecka.nu, but this requires opening a web browser
and going to the site specified - assuming that one can remember the address. The
goal of this it to make this data available on the local machine, instead.

TO RUN:
    python SvenskaVeckanNummer.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2018"
__license__ = "MIT"

import datetime

today = datetime.date.today()

# Since the ISO Calendar object is an array in Python, we return the object in the array representing the week's number.
week_number = today.isocalendar()[1]
print(week_number)
