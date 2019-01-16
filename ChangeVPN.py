#!/usr/bin/env python
"""Randomly connections to a random VPN profile (if any are found).

Uses NetworkManager (https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.html#) to
enumerate the devices and connections. First, we enumerate the wireless devices to ensure that we have one. Next, we
enumerate the VPN connections and put them into a list. After that, we randomly select one of the VPN connections to
connect to. Once we've accomplished this, we disconnect the current VPN connection (if one is found) and connect to
the randomly chosen VPN connection.

REQUIREMENTS:
    python-networkmanager

TO RUN:
    python NetworkManager_VPN.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import os
import random
import time
# Externals
import NetworkManager

# Find all of the VPN connections on the machine.
vpns = list()
current_vpn = None
wireless_device = None
connections = NetworkManager.Settings.ListConnections()
for c in connections:
    if "vpn" in c.GetSettings()['connection']['type']:
        path = c.object_path
        vpns.append(path)

# If there are no VPN connections, there's no point in proceeding.
if vpns.__len__() > 0:
    # We find the Wireless Network Interface.
    # If you're running some kind of weird, three wireless network cards situation, then...
    # Change this code to work in your use-case scenario.
    devices = NetworkManager.Device.all()
    for d in devices:
        if "wifi" in d.Driver:
            wireless_device = d

    # Validate that we found a wireless network interface
    if wireless_device is not None:
        # Get the currently active VPN connection.
        # If you're running some kind of weird, three active VPNs scenario, then...
        # Change this code to work in your use-case.
        active = NetworkManager.NetworkManager.ActiveConnections
        for a in active:
            if "vpn" in a.Type:
                current_vpn = a

        # Choose a random one to connect to. We use the far more secure random method, with a larger seed,
        # to try and prevent the random generation from being a predictable pattern (well, to try to make
        # it far less predictable with our sample, at least).
        rand = random.SystemRandom(os.urandom(99999999))
        random_int = rand.randint(0, (vpns.__len__() - 1))
        random_vpn = vpns.__getitem__(random_int)
        new_connection = NetworkManager.Connection(random_vpn)

        # Validate that we have a current VPN connection to disconnect from before we do.
        if current_vpn is not None:

            # Disconnect the old & busted.
            NetworkManager.NetworkManager.DeactivateConnection(current_vpn)

            # To prevent collision in NetworkManager, we allow background clean-up before reconnecting.
            time.sleep(10)

        # Connect the new hotness.
        print("Connecting to: {}".format(random_vpn))
        NetworkManager.NetworkManager.ActivateConnection(new_connection, wireless_device, "/")

    # No wireless interfaces were found, so let's abort.
    else:
        raise Exception("No wireless interfaces were found.")

# No VPN connections were found, so let's abort.
else:
    raise Exception("The hull has been breached and the science is leaking out! "
                    "(We didn't find any valid VPN connections on this machine via NetworkManager.)")
