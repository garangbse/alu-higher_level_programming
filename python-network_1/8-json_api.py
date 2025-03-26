#!/usr/bin/python3
import requests
import sys


"""
Script that sends a POST request to search for a user
"""


if __name__ == "__main__":
    # Get the letter from command line argument or use empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Define the URL and payload
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        # Send POST request
        response = requests.post(url, data=payload)
        
        # Try to parse JSON response
        try:
            json_response = response.json()
            
            # Check if response is empty
            if json_response:
                print("[{}] {}".format(
                    json_response.get('id'),
                    json_response.get('name')
                ))
            else:
                print("No result")
                
        except ValueError:
            print("Not a valid JSON")
            
    except Exception as e:
        print(e)
