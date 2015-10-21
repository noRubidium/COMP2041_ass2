#!/usr/bin/python
import cgi, cgitb
import Search,Html
import json
from StringIO import StringIO

print "Content-Type: application/json"
print

form = cgi.FieldStorage()
if "bleats_recursive" in form.keys():
	bleat = Search.search_bleat_by_bleat_ID(form["bleats_recursive"].value)
	queue = list()
	queue.append(bleat.bleat_No)
	result = list()
	io = StringIO()
	while not len(queue) == 0:
		bleat_No = queue.pop(0)
		bleats = Search.search_bleat_by_in_reply_to(bleat_No)
		for bleat in bleats:
			queue.append(bleat.bleat_No)
			result.append(vars(bleat))
	json.dump(result,io)
	print io.getvalue()
elif "username" in form.keys():
	user = Search.search_user_by_ID_e(form["username"].value)
	print json.dumps(vars(user))