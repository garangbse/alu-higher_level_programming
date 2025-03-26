#!/bin/bash
# Script that sends a GET request with custom header and displays response body
curl -H "X-HolbertonSchool-User-Id: 98" -s "$1"
