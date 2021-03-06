# Python
Several scripts written in Python, to accomplish varying tasks.

## AnförandeniSenasteDagen.py
Uses the [Requests](https://docs.python-requests.org/en/master/) package to query the [Riksdagen](https://www.riksdagen.se/) (specifically, the [Riksdagen's API](https://data.riksdagen.se/)) for any speeches (Anföranden) posted in the past day and, if any are found, it prints the Document ID, Title, and URL to each speech in question.

## ChangeVPN.py
Randomly connects to a VPN connection on the wireless interface via [NetworkManager](https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.html#).

## CheckSockets.py
Enumerates through ports (0-65534) and attempts to open a socket on each one. If blocked, the socket is added to a list and then we attempt to find out what process, precisely, is currently utilising that socket.

## MacChaningDaemon.py
Creates a daemon to change the mac address on an interface once per hour (far too aggressive, I'm aware).

## ModifyOvpnConfigurations.py
Modifies the OVPN configuration files referenced by NetworkManager with the username and password, changing the connection to autologin.

## ObfuscatePhotos.py
Imports the byte data from photo a given photo and applies a transformation to it to make it useless to AI. See the [before](https://github.com/felsokning/Python/blob/master/PhotoData/PhU2GL.jpg) and [after](https://github.com/felsokning/Python/blob/master/PhotoData/test.jpg) to understand the context.
As an FYI: Google believes the after photo to be "[fondos de pantalla pc](https://www.solofondos.com/fondos-de-pantalla-pc.html)"

## RemoveSyntolkat.py
Removes [Syntolkat](https://en.wikipedia.org/wiki/Audio_description) files from a given path.

## RemoveVPNs.py
Uses [NetworkManager](https://developer.gnome.org/NetworkManager/stable/gdbus-org.freedesktop.NetworkManager.html#) to enumerate all of the VPN profiles and then deletes them.

## RenameSrtFiles.py
Finds SRT (SubRip Text) files that do not contain the given [ISO 639-2 Code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) and renames them to include the given code.

## ScanForAPs.py
Periodically scans for new access points available to the wireless network interface and prints any new found access points to the terminal.

## SvenskaVeckanNummer.py
Original skeleton for the script that's used in Docker (see: Docker/SwedishWeekNumber)

## SwedishDate.py
Class meant to be imported and used to return the ISO week number from a given date.
