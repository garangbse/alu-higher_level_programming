import sys

#!/usr/bin/python3
"""Script that fetches URL and handles HTTP errors"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
