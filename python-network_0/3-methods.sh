#!/bin/bash
# Script to display HTTP methods accepted by the server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
