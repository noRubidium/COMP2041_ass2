#!/usr/bin/python
import cgi, cgitb
import Search,Html
print "Content-Type: text/json"
print
print

form = cgi.FieldStorage()
if "bleats_recursive" in form.keys():
	bleat = Search.search_bleat_by_bleat_ID(form["bleats_recursive"].value)
	queue = list()
	queue.append(bleat.bleat_No)
	while not len(queue) == 0:
		bleat_No = queue.pop(0)
		bleats = Search.search_bleat_by_in_reply_to(bleat_No)
		for bleat in bleats:
			queue.append(bleat.bleat_No)
			print Html.print_json(bleat)
			print ","
