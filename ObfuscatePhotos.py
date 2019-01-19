#!/usr/bin/env python
"""Modifies a photo data to have Poisson and Exponential noise and saves the resultant to a new file.

This imports the byte data (as an ndparray) and performs two translations on the file data. First, we apply a Poisson
randomisation (https://en.wikipedia.org/wiki/Poisson_distribution#Generating_Poisson-distributed_random_variables). We
then apply an exponential against the set to modify the overall photo. We then save that data as a new file.

NOTE:
    Since scipy has deprecated their image modification methods, this was the first I found to work.
    I have supplied two examples in this repo, under the PhotoData folder, of a before and after. Even though can discern
    what the after photo is, if you feed it into Google's image search, it will think that it is
    "fondos de pantalla pc" - which is the desired result of this script: To obfuscate the data to make it useless to
    AI but still perceptibe to humans.

TO RUN:
    python[3] ObfuscatePhotos.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import imageio
import numpy
import os
import scipy

filename = '/PhotoData/PhU2GL.jpg'
image_data = (imageio.imread(filename)).astype('uint8')
noise_mask = numpy.random.poisson(image_data)
noisy_mask = (numpy.random.exponential(noise_mask)).astype('uint8')
imageio.imwrite('/home/renholder/Bilder/test.jpg', noisy_mask)
