#!/usr/bin/env python
"""Removes all VPN profiles found in NetworkManager.

Uses NetworkManager (https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.html#) to
enumerate the connections that are specifically VPN connections. Then, we delete them, with righteous retribution and
indignation.

REQUIREMENTS:
    python-networkmanager

TO RUN:
    python3 RemoveVPNs.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import NetworkManager

# Find all of the VPN connections on the machine.
vpn_list = list()
connections = NetworkManager.Settings.ListConnections()
for c in connections:
    if "vpn" in c.GetSettings()['connection']['type']:
        vpn_list.append(c)

# We make sure we'e not spinning our wheels and/or calling delete on null.
if len(vpn_list) > 0:
    for v in vpn_list:
        print("Deleting: {}".format(v.object_path))
        v.Delete()
