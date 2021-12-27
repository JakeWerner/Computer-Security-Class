#!/usr/bin/python3

import sys
from urllib.parse import quote, quote_from_bytes, urlparse
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here

    # Obtain input url and parse to obtain everything after '?' in the URL:
    res = urlparse(url)
    query = res.query

    # Isolate token and command(s) from query
    params = query.split('&', maxsplit=1)
    token = params[0][6:]
    commands = params[1]
    
    # Create message from concatenating all the command(s)
    m = commands
    len_of_m = len(m)
    # Calculate padding for secret + message
    bits = (8 + len_of_m + len(padding(8*8 + len_of_m * 8))) * 8
    # Create new md5 object and add "UnlockSafes" command to the message
    h = md5(state = bytes.fromhex(token), count=bits)
    newCommand = "&command=UnlockSafes"
    h.update(newCommand)
    # Create new token from resulting hash of the length extended message
    newToken = h.hexdigest()

    # Create new URL built from parts of given URL
    newURL = res.scheme + "://" + res.netloc + res.path + "?token=" + newToken + "&" + commands
    # Calculate hexadecimal for padding of secret + message
    pad = padding(8*8 + len_of_m * 8)
    # Add padding to the new URL with the desired command "&command=UnlockSafes"
    newURL = newURL + quote(pad) + "&command=UnlockSafes"
    print(newURL)