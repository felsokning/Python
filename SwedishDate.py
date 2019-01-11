#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Returns the current week number of the year.

As some countries (e.g.: Sweden) use week numbers for organisation, it's
important to be able to return the week number in an easily referenced
code-base.

NOTE:
    Use SwedishDate instead of datetime.date to leverage this.
    import SwedishDate

    SwedishDate.today().veckan()
    SwedishDate(1990, 10, 10).veckan()
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__credits__ = "Peter Saverman"

from datetime import date


# Vi har att skapa en ny klass eftersom python har inte "extensions methods"
class SwedishDate(date):
    # Vi skulle heter det på svenska, nej?
    def veckan(self):
        return self.isocalendar()[1]
