import sys

#!/usr/bin/python3
"""
Script that takes a URL, sends a request and displays X-Request-Id from header
"""
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
