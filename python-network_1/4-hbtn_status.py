import requests

#!/usr/bin/python3
"""Script that fetches https://alu-intranet.hbtn.io/status using requests package"""


def fetch_status():
    """Fetches the status from ALU intranet"""
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
