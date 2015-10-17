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
		
		if 'action' in form.keys() and form['action'].value== "POST":
			content = special_char_filter.special_char_filter(form['bleat_content'].value) 
			#try every value which can be blank
			try:
				in_reply_to = form["in_reply_to"].value
			except:
				in_reply_to = ""
			try:
				latitude = form["latitude"].value
			except:
				latitude = ""
			try:
				longitude = form["longitude"].value
			except:
				longitude = ""
			import datetime
			dt = (datetime.datetime.now()-datetime.datetime(1970,1,1))
			time = dt.days * 1440*60 + dt.seconds
			#Update the bleats database
			conn = sqlite3.connect('database/Bleats.db')
			c = conn.cursor()
			data = (username,content,in_reply_to,time,longitude,latitude,"")
			c.execute( '''INSERT INTO bleats VALUES(null,?,?,?,?,?,?,?)''',data)
			operation="SELECT bleatID FROM bleats WHERE username = ? AND bleat = ? AND time = ?;"
			conn.commit()
			selection=(username,content,time)
			c.execute(operation,selection)
			bleatID = str(c.fetchone()[0])
			conn.close()
			# Update the user database
			user = Search.search_user_by_ID_e(username)
			user.add_bleats(bleatID)
			user.update()
			user.main_page()
			print user.user_display()
		else:
			#print the default empty send bit page
			try:
				in_reply_to = form["in_reply_to"]
			except:
				in_reply_to =""
			print open(base+"send_bleats.html").read().format(in_reply_to);
	#if the user is not logged in: print the primary page
	else:
		print 
		print 
		print Html.header("Bitter").__str__()
		print Html.login_page_display()
#If there's no cookie means the user wasn't logged in
except (Cookie.CookieError, KeyError):
	print 
	print
	print Html.header("Bitter").__str__()
	print Html.login_page_display()

print Html.footer().__str__()
