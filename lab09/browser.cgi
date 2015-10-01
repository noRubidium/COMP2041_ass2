#!/bin/sh
echo Content-type: text/html
echo

host_address=`host $REMOTE_ADDR 2>&1|grep Name|sed 's/.*: *//'`
add=$REMOTE_ADDR
name=`host "$add"`
name=`echo "$name" |sed 's/.* name pointer//' | sed 's/\.[\s\t]*$//'`
cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>IBrowser IP, Host and User Agent</title>

</head>
<body>
Your browser is running at IP address: <b>$add</b>
<p>
Your browser is running on hostname: <b>$name</b>
<p>
Your browser identifies as: <b>$HTTP_USER_AGENT</b>
</body>
</html>
eof
