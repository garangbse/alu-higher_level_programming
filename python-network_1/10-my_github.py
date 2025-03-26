import requests
import sys

#!/usr/bin/python3
"""
Script that takes GitHub credentials and displays user id
using GitHub API with Basic Authentication
"""

if __name__ == "__main__":
    # Get username and token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for user information
    url = "https://api.github.com/user"

    # Create Basic Authentication header using username and token
    auth = (username, token)

    # Send GET request to GitHub API
    response = requests.get(url, auth=auth)

    # Check if request was successful and print user id
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")
