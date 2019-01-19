#!/usr/bin/env python
"""Changes the exported OVPN configurations in NetworkManager to contain the username and password and autoconnect.

When mass-importing OVPN configuration files, it's necessary to overcome the hurdle of the prompt for passwords. This
script looks for the exported configuration files in NetworkManager. It writes the password configuration and the
username/password to the file. You will need to restart NetworkManager for the changes to be imported; however, it's
easier/better just to bounce the machine. (sudo init 6)

TO RUN:
    sudo python3 ModifyOvpnConfigurations.py
"""

__author__ = "felsokning"
__copyright__ = "Copyright 2019"
__license__ = "MIT"

import os
import re

source_directory = "/etc/NetworkManager/system-connections"
ovpn_files = os.listdir(source_directory)
i = 0
for ovpn in ovpn_files:
    opened_file = open(source_directory + "/" + ovpn, "r+")
    file_content = opened_file.read()
    if file_content.__contains__("mssfix=1450\n"):
        output = re.sub(r"mssfix=1450", r"mssfix=1450\npassword-flags=0", file_content)
        # TODO: Change '*' to be your username
        output2 = re.sub(r"tunnel-mtu=1500", "tunnel-mtu=1500\nusername=*", output)
        output3 = re.sub(r"service-type=org.freedesktop.NetworkManager.openvpn", r"service-type=org."
                                                                                 r"freedesktop.NetworkManager."
                                                                                 r"openvpn\n\n[vpn-secrets]\n"
                                                                                 # TODO: Change '*' to your VPN password
                                                                                 r"password=*\n",
                         output2)
        output4 = re.sub(r"password-flags=1", r"", output3)

        # Indents are important, m'kay? Without them, you do things like overwrite your wireless config files.
        # Take it from me: You do NOT want to do that.
        opened_file.truncate(0)
        opened_file.seek(0)
        opened_file.write(output4)
        opened_file.close()
        print(ovpn)
