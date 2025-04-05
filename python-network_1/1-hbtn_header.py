import sys

#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
