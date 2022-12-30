#!/bin/bash
# Read a file containing URLs and invoke curl to visit those URLs

# Check if file argument is present
if [ -z $1 ]; then
    echo "No file provided. Please provide a file containing URLs."
    exit 1
fi

# Read file line by line
while read line; do
    # Check if line is a valid URL
    if [[ $line == http* ]]; then
        # Visit the URL
        curl -k $line
    fi
done < $1