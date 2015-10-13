#!/bin/sh
MAX=5
# Run from webserver.sh to handle a single http request
read http_request || exit 1
cd ~
cd public_html
add=`echo "$http_request"|cut -d/ -f2-|cut -d" " -f1`

status_line="HTTP/1.0 200 OK"
content_type="text/html"
head=`cat "test.html"`
tail=`cat "test_tail.html"`
if `echo "$add" | grep -q "[0-9]"`
then
	add=`echo "$add" | grep -Eo '[0-9]+'`
else
	add=`expr $RANDOM % 3000`
fi

i=1
content="$head factors of $add</h2><pre>"
while [ $i -le $add ]
do
	if [ `expr $add % $i` -eq 0 ]
	then 
		content="$content <a href=\"$i.html\">$i.html</a></p>"
	fi
	i=`expr $i + 1`
done
i=2
while [ $i -le $MAX ]
do
	num=`expr $i \* $add`
	content="$content <a href=\"$num.html\">$num ( $add * $i )</a></p>"
	i=`expr $i + 1`
done
content="$content <a href=\"index.html\">index.html</a></p>$tail"
content_length=`echo "$content"|wc -c`

echo "HTTP/1.0 200 OK"
echo "Content-type: $content_type"
echo "Content-length: $content_length"
echo
echo "$content"
exit 0
