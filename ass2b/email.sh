#!/bin/sh
msg=$1
address=$3
title=$2
#echo "$msg"|mutt -s "$title" -- "$address"
echo "Content-Type: text/html"
echo
echo
echo "Hello"|mutt -s "Test" -- "markshen5295@gmail.com"
echo Testing
