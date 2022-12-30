#!/bin/bash

# create a file to store the visited urls
touch visited_urls.txt

# read the file containing the urls
while read url; do
  # use curl to visit the url
  response_code=$(curl -s -o /dev/null -w "%{http_code}" $url)
  
  # save the url to the visited urls file based on the returned response code
  if [ $response_code -eq 200 ]; then
    echo $url >> visited_urls.txt
  fi
done <urls.txt