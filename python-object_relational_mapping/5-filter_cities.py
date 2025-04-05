#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to it and displays
the value of the X-Request-Id variable found in the header
"""

import requests
import sys


if __name__ == "__main__":
    # Get URL from command line arguments
    url = sys.argv[1]

    # Send request to the URL
    response = requests.get(url)

    # Display the value of X-Request-Id from the response header
    print(response.headers.get('X-Request-Id'))
