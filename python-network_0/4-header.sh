#!/bin/bash
# Script that sends a GET request with custom header and displays response body
curl -sH "X-School-User-Id: 98" "$1"