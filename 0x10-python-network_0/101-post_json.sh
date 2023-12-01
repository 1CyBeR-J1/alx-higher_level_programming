#!/bin/bash
#sends JSON POST request to URL passed as 1st arg displays body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
