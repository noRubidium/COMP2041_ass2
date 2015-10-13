#!/bin/sh
echo Content-type: text/html
echo

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>Environment Variables</title>
</head>
<body>

Here are the environment variables the web server has passed to this CGI script:
<pre>
eof

env

cat <<eof
</pre>
</body>
</pre>
</html>
eof
