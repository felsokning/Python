#!/usr/bin/env python
"""Periodically scans for access points and prints new ones.

Uses NetworkManager (https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.html#) to
find the wireless device, requests a scan for wireless access points, and then obtains the list of the access points
returned. It then ensures whether the access point has been seen before and, if not, prints the SSID and BSSID on the
screen.

TODO:
    Find a way to resolve the copy issue, which is causing the NetworkManager.ObjectVanished exception to be thrown.

REQUIREMENTS:
    python-networkmanager

TO RUN:
    python ScanForAPs.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import copy
import dbus
import time

# Externals
import NetworkManager

found_access_points = list()

while True:
    # We find the Wireless Network Interface.
    # If you're running some kind of weird, three wireless network cards situation, then...
    # Change this code to work in your use-case scenario.
    devices = NetworkManager.Device.all()
    for d in devices:
        if "wifi" in d.Driver:
            wireless_device = d

    if wireless_device is not None:
        try:
            last_scan = wireless_device.RequestScan({})
            time.sleep(1)

            # Assignment statements in Python do not copy objects, they create bindings between a target and an object.
            # For this reason, we run into NetworkManager.ObjectVanished exceptions because the objects referenced by
            # the pointers are disposed of, so we can't access the data, anymore. Fun times...
            # I haven't figured out a way around this, as copy.deepcopy doesn't create unique AccessPoint objects, with
            # unique properties, in the new list. Problematic? To be sure...
            deep_copy_access_points = copy.deepcopy(wireless_device.AccessPoints)
            for ap in deep_copy_access_points:
                if not found_access_points.__contains__(ap):
                    found_access_points.append(ap)
                    if ap.Ssid is not None:
                        print("{0} {1}".format(ap.Ssid, ap.HwAddress))
                    else:
                        print("{}".format(ap.HwAddress))
        except dbus.DBusException as dbusEx:
            print(dbusEx.message)
        except NetworkManager.ObjectVanished as ovEx:
            print("Object vanished...")

    time.sleep(60)
