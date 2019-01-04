#!/usr/bin/env python
"""Checks for open sockets and then lists the corresponding processes.

Uses socket to iterate from 0 to 65534 and attempts to create a socket on the
specified number. If the socket is failed to be created (Error98), we store the socket
number in a list. We then iterate through that list to create a string, passing that string
to the lsof command, as it does not require elevation to run.

TO RUN:
    sudo python SocketsCheck.py
"""

import os
import socket

__author__ = "felsokning"
__copyright__ = "Copyright 2018"
__license__ = "MIT"


def check_sockets():
    new_list = list()
    for i in range(0, 65534):
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Try to open port
            new_socket.bind(('', i))
        except OSError as e:
            # Error 98 infers that the socket is already bound
            if e.errno is 98:
                # We only care about listing the open ones.
                opened = i
                new_list.append(opened)
        new_socket.close()
    return new_list


returned_list = check_sockets()
ports_string = str()
for x in returned_list:
    ports_string = ports_string + "{},".format(x)
os.system('lsof -i :{}'.format(ports_string))

