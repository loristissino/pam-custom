#!/bin/bash
# This is just an example, to show that you get the provided username 
# and password
# We just log them, and exit with 1 (means auth is NOT ok)

USER="$1"
PASSWORD="$2"

echo $USER:$PASSWORD >> /tmp/logchecks.txt

exit 1
