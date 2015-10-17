#!/bin/sh
msg=$1
address=$3
title=$2
echo "$msg"|mutt -s "$title" -- "$address"
echo "HI"
echo "$msg"
echo $address
echo $title