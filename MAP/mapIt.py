#! python2.7
#  mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser,sys,pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ''.join(sys.argv[1:])
else:
	address = pyperclip.paste()
# TODO: Get address from clipboard.

webbrowser.open('https://www.google.com/maps/place/' + address)

