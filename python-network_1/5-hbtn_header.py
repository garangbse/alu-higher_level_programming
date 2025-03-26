import requests
import sys

#!/usr/bin/python3
"""
Script that sends a request to a URL and displays X-Request-Id header value
"""

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))