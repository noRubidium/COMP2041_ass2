#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
import Search,login_validate
import special_char_filter
import sqlite3
print "Content-Type: text/html"
base = "html/"

try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	username = cookie["username"].value
	form = cgi.FieldStorage()
	if login_validate.validate(cookie["logged_in"].value):
		if 'action' in form.keys():
			action = form["action"].value
			print cookie.output()
			print
			print Html.header("Bitter")
			print Html.nav_bar_display(username)
			if action == "save_change":
				if "pic_dir" in form.keys():
					picture = form["pic_dir"]
					if picture.filename:
						open("user_bg/"+username+"_bg.jpg", 'w').write(picture.file.read())
				user = Search.search_user_by_ID_e(username)
				user.main_page()
				print user.user_display()
			elif action == "delete":
				if os.path.isfile("user_bg/"+username+"_bg.jpg"):
					os.remove("user_bg/"+username+"_bg.jpg")
			else:
				bg_path = "user_bg/"+username+"_bg.jpg"
				if not os.path.isfile(bg_path):
					bg_path=""
				print open(base+"change_bg.html").read().format(bg_path);
		

		else:
			print cookie.output()
			print
			print Html.header("Bitter")
			print Html.nav_bar_display(username)
			bg_path = "user_bg/"+username+"_bg.jpg"
			if not os.path.isfile(bg_path):
				bg_path=""
			print open(base+"change_bg.html").read().format(bg_path);
	#if the user is not logged in: print the primary page
	else:
		print 
		print 
		print Html.header("Bitter")
		print Html.login_page_display()
#If there's no cookie means the user wasn't logged in
except (Cookie.CookieError, KeyError):
	print 
	print
	print Html.header("Bitter")
	print Html.login_page_display()

print Html.footer()
