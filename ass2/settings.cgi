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
		if 'action' in form.keys():
			username = cookie["username"].value
			action = form["action"].value
			if action == "save_change":
				print cookie.output()
				print
				print Html.header("Bitter")
				print Html.nav_bar_display(username)
				# Update the user class
				user = Search.search_user_by_ID_e(username)
				if "pic_dir" in form.keys():
					picture = form["pic_dir"]
					if picture.filename:
						user.pic_path = "user_img/"+username+"_profile.jpg"
						open("user_img/"+username+"_profile.jpg", 'w').write(picture.file.read())
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
				# update the database
				user.update()
				user.main_page()
				print user.user_display()
			
			# Apparently it is deleting the user profile picture
			elif action == "delete_pic":
				print cookie.output()
				print
				print Html.header("Bitter")
				print Html.nav_bar_display(username)
				# Update the user database
				user = Search.search_user_by_ID_e(username)
				try:
					if not user.pic_path == "img/default.jpg":
						os.remove(user.pic_path)
				except:
					pass
				user.pic_path = "img/default.jpg"
				user.update()
				user.main_page()
				print user.user_display()
			
			# delete the whole user
			elif action == "delete":
				# DELETE the user account
				operation = "DELETE FROM users WHERE username = ?;"
				import sqlite3
				user = Search.search_user_by_ID_e(username)
				conn = sqlite3.connect("database/User.db")
				c = conn.cursor()
				c.execute(operation,(username,))
				conn.commit()
				c.close()
				conn.close()
				conn = sqlite3.connect("database/Bleats.db")
				c = conn.cursor()
				for bleat in user.bleats:
					operation = "DELETE FROM bleats WHERE bleatID= ?;"
					c.execute(operation,(bleat,))
				conn.commit()
				c.close()
				conn.close()
				cookie["logged_in"] = 0
				print
				print
				print Html.login_page_display()
			else:
				print cookie.output()
				print
				print Html.header("Bitter")
				print Html.nav_bar_display(username)
				user= Search.search_user_by_ID_e(username)
				if user.is_suspended:
					check="checked"
				else:
					check=""
				print open(base+"edit_user.html").read().format(user.email,user.username,user.full_name,
					user.password,user.pic_path,user.longitude,user.latitude,user.suburb,user.status,
					user.UID,user.listens,user.bleats,check);
				print """<script>
				$(document).ready(function(){
					$("img").addClass("img-responsive");
					});
				</script>"""
		else:
			print cookie.output()
			print
			print Html.header("Bitter")
			username = cookie["username"].value
			print Html.nav_bar_display(username)
			user= Search.search_user_by_ID_e(username)
			if user.is_suspended:
				check="checked"
			else:
				check=""
			print open(base+"edit_user.html").read().format(user.email,user.username,user.full_name,
				user.password,user.pic_path,user.longitude,user.latitude,user.suburb,user.status,
				user.UID,user.listens,user.bleats,check);
			print open(base+"page.html").read()
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
