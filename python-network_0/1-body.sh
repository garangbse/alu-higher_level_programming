#!/bin/bash
# Script that sends GET request and displays body of 200 status code response
curl -s -L -w "%{http_code}" "$1" | grep -v "^200$" || curl -s -L "$1"
