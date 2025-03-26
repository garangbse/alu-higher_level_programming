#!/usr/bin/python3
import requests
import sys


"""
Script that takes in a URL, sends a request and displays the body of the response.
Handles HTTP status codes >= 400 by printing the error code.
"""

if __name__ == "__main__":
    url = sys.argv[1]
    
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
