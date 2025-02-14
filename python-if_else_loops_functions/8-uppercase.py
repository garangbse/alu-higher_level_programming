#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Convert character to uppercase if it's lowercase (a-z)
        # ASCII 'a' = 97, 'z' = 122, difference to uppercase is 32
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    