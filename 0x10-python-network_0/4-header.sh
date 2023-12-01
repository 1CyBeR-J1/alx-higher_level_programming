#!/bin/bash
#takes URL as arg, sends GET request to URL, and displays the body of response
curl -sH "X-School-User-Id: 98" "$1"
