# Python
Several scripts written in Python, to accomplish varying tasks.

## ChangeVPN.py
Randomly connects to a VPN connection on the wireless interface via NetworkManager.

## CheckSockets.py
Enumerates through ports (0-65534) and attempts to open a socket on each one. If blocked, the socket is added to a list and then we attempt to find out what process, precisely, is currently utilising that socket.

## MacChaningDaemon.py
Creates a daemon to change the mac address on an interface once per hour (far too aggressive, I'm aware).

## SvenskaVeckanNummer.py
Original skeleton for the script that's used in Docker (see: Docker/SwedishWeekNumber)
