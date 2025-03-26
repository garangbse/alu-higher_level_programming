#!/bin/bash
# Takes a URL, sends a request and returns the size of the response body in bytes
curl -s "$1" | wc -c
