import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves to a file"""

filename = "add_item.json"

# Initialize the list
my_list = []

# Load existing data if file exists
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
