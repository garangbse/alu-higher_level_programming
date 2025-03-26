#!/usr/bin/python3
import sys


"""
Script that sends a POST request to a URL with an email parameter
and displays the response body
"""
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create the request and send it
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        print(response.read().decode('utf-8'))
