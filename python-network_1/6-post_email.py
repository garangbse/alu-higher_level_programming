import requests
import sys

#!/usr/bin/python3
"""
Script that sends a POST request to a URL with an email parameter
and displays the response body
"""

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Create payload dictionary with email parameter
    payload = {'email': email}
    
    # Send POST request with email parameter
    response = requests.post(url, data=payload)
    
    # Display response body
    print(response.text)
