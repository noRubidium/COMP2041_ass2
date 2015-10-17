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
	form = cgi.FieldStorage()
	if login_validate.validate(cookie["logged_in"].value):
		print cookie.output()
		print
		print Html.header("Bitter")
		username = cookie["username"].value
		print Html.nav_bar_display(username)
		
		if 'action' in form.keys():
			action = form["action"].value
			if action == "save_change":
				# Update the user database
				user = Search.search_user_by_ID_e(username)
				if "pic_dir" in form.keys():
					picture = form["pic_dir"]
					if picture.filename:
						if user.pic_path == "":
							user.pic_path = "user_img/"+username+"_profile.jpg"
							open(user.pic_path, 'w').write(picture.file.read())
						else:
							open(user.pic_path, 'w').write(picture.file.read())
				if "longitude" in form.keys():
					user.longitude = form["longitude"].value
				if "latitude" in form.keys():
					user.latitude = form["latitude"].value
				if "suburb" in form.keys():
					user.suburb = form["suburb"].value
				if "status" in form.keys():
					user.status = form["status"].value
				if "suspend" in form.keys():
					user.is_suspended = True
				else:
					user.is_suspended = False
				user.update()
				user.main_page()
				print user.user_display()
			elif action == "delete":
				pass
			else:
				user= Search.search_user_by_ID_e(username)
				if user.is_suspended:
					check="checked"
				else:
					check=""
				print open(base+"edit_user.html").read().format(user.email,user.username,user.full_name,
					user.password,user.pic_path,user.longitude,user.latitude,user.suburb,user.status,
					user.UID,user.listens,user.bleats,check);
		else:
			user= Search.search_user_by_ID_e(username)
			if user.is_suspended:
				check="checked"
			else:
				check=""
			print open(base+"edit_user.html").read().format(user.email,user.username,user.full_name,
				user.password,user.pic_path,user.longitude,user.latitude,user.suburb,user.status,
				user.UID,user.listens,user.bleats,check);
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
