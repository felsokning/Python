#!/usr/bin/env python
"""Changes the MAC Address of a given interface.

Uses netifaces to validate the adapter is found, disables the interface, uses
macchanger to change the mac address, disables the NetworkManager, enables the
NetworkManager, and then brings the interface back up.

NOTE:
    macchanger must be installed on your flavour of *nix.
    python-daemon must be installed via pip
    netifaces must be installed via pip
TO RUN:
    sudo python MacChanger.py
"""

import logging
import logging.handlers
import os
import time as ti
# Externals
import daemon
import netifaces as ni

__author__ = "felsokning"
__copyright__ = "Copyright 2018"
__license__ = "MIT"

wireless_interface = 'wlp1s0'
vpn_identity = 'eb5d9fa5-99b9-4e00-89dd-b57a44378e02'


def main():
    file_logger = logging.FileHandler("/tmp/daemon.log", "w")
    logger = logging.getLogger()
    logger.addHandler(file_logger)
    logger.setLevel(logging.INFO)

    # Run FOREVER
    while True:
        logger.info("Ran at: {}".format(ti.ctime()))
        if ni.ifaddresses('wlp1s0'):
            # Bring the VPN down
            log_string = "Bringing VPN {} down at: {}".format(vpn_identity, ti.ctime())
            logger.info(log_string)
            command = "sudo nmcli con down {}".format(vpn_identity)
            os.system(command)

            # Now sleep for one second
            ti.sleep(1)

            # Bring the interface down
            log_string = "Bringing interface {} down at: {}".format(wireless_interface, ti.ctime())
            logger.info(log_string)
            os.system('sduo ip link set {} down'.format(wireless_interface))

            # Bring networking down
            logger.info("Tearing Network Manager down at: {}".format(ti.ctime()))
            os.system('sudo systemctl stop NetworkManager.service')

            # Now sleep for one second
            ti.sleep(1)
            log_string = "Changing MAC Address on {} at: {}".format(wireless_interface, ti.ctime())
            logger.info(log_string)

            # Change the mac address
            os.system('sudo macchanger -r {}'.format(wireless_interface))
            # Now sleep for one second
            ti.sleep(1)

            # Bring the interface back up
            log_string = "Bringing interface {} up at: {}".format(wireless_interface, ti.ctime())
            logger.info(log_string)
            os.system('sudo ifconfig {} up'.format(wireless_interface))

            # Now sleep for one second
            ti.sleep(1)

            # Bring networking up
            logger.info("Bringing Network Manager back up at: {}".format(ti.ctime()))
            os.system('sudo systemctl start NetworkManager.service')

            # Now sleep for twenty seconds for negotiation on WiFi interface
            ti.sleep(20)

            # Bring the VPN back up
            log_string = "Bringing VPN {} back up at: {}".format(vpn_identity, ti.ctime())
            logger.info(log_string)
            command = "sudo nmcli con up {} passwd-file ~/Dokument/openVpn/pass.txt".format(vpn_identity)
            os.system(command)

            # Now sleep for an hour
            ti.sleep(3600)
        else:
            logger.info("Interface {} not found.".format(wireless_interface))


with daemon.DaemonContext():
    main()

