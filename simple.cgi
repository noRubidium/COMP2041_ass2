#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au

echo Content-type: text/html
echo
echo '<html><head></head><body><h2>Execution Environment</h2><pre>'

for command in pwd id hostname 'uname -a'
do
    echo "$command: `$command`"
done

echo '</pre></body></html>'
