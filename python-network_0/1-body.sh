#!/bin/bash
# Script that sends GET request and displays body of 200 status code response
curl -sfL "$1" -X GET
