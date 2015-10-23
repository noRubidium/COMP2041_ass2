#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
import Search,login_validate
import special_char_filter
print "Content-Type: text/html"
base = "html/"
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	if login_validate.validate(cookie["logged_in"].value):
		print cookie.output()
		print
		print Html.header("Bitter").__str__()
		username = cookie["username"].value
		print Html.nav_bar_display(username)
		form = cgi.FieldStorage()
		if "action" in form.keys():
			action = form["action"].value
			if "bleat_No" in form.keys():
				bleat_No = form["bleat_No"].value
				bleat = Search.search_bleat_by_bleat_ID(bleat_No)
				if bleat.exist:
					if action == "full_display":
						author = Search.search_user_by_ID_e(bleat.author);
						string = author.user_info()
						queue = list()
						queue.append(bleat.bleat_No)
						replies = ""
						while not len(queue) == 0:
							bleat_No = queue.pop(0)
							bleats = Search.search_bleat_by_in_reply_to(bleat_No)
							for bleat in bleats:
								queue.append(bleat.bleat_No)
								replies += bleat.format_bleat()
						print open(base+"full_bleat.html").read().format(bleat.print_loc_row(),
							bleat.print_reply(),bleat.format_content(),bleat.author,
							bleat.time,bleat.bleat_No,string,replies,bleat.print_attachment())
						print open(base+"style_bleat.html").read()
						if "del_notice" in form.keys():
							mentioned = Search.search_notification_by_username(username)
							mentioned.del_mentioned(bleat_No)
							mentioned.update()
					elif action == "delete" and bleat.author == username:
						import sqlite3
						# Delete from user's bleat list
						# conn = sqlite3.connect('database/User.db', timeout=10)
						# c = conn.cursor()
						# print username
						# operation="SELECT bleats FROM users WHERE username = '{0}';".format(username)
						# c.execute(operation);
						# w = c.fetchone();
						# import re;
						# operation="UPDATE users SET bleats='{1}' WHERE username= '{0}' ".format(username,re.sub(str(bleat_No),"",w[0]))
						# c.execute(operation,)
						
						# conn.commit()
						# c.close()
						# conn.close()
						# Delete from bleats list
						conn = sqlite3.connect('database/Bleats.db', timeout=10)
						c = conn.cursor()
						operation = "DELETE FROM bleats where bleatID = {0};".format(bleat_No)
						c.execute(operation)
						conn.commit()
						c.close()
						conn.close()
						print "<h2>The bleat has been deleted successfully</h2>"
				else:
					print open(base+"404.html").read()
			else:
				#print the default empty search page
				print open(base+"404.html").read()
		else:
			#print the default empty search page
			print open(base+"404.html").read()
		print Html.footer()
	else:
		print 
		print
		print Html.header("Bitter")
		print Html.login_page_display()
		print Html.footer()
except (Cookie.CookieError, KeyError):
	print 
	print
	print Html.header("Bitter")
	print Html.login_page_display()
	print Html.footer()
