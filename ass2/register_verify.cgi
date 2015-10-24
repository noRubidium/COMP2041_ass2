#!/usr/bin/python
import cgi, cgitb
import Html,Search
import sqlite3,os

print "Content-Type: text/html"
print
print
form = cgi.FieldStorage()
print Html.header("Bitter")
if 'key' in form.keys():
	key = form['key'].value
	user = Search.search_tmp_user_by_key(key)
	if user.exist:
		username=user.username
		full_name=user.full_name
		email=user.email
		listens=' '.join(user.listens)
		password=user.password
		home_longitude = user.longitude
		home_latitude = user.latitude
		home_suburb = user.suburb
		picture_dir = user.pic_path
		if os.path.isfile("tmp/"+key):
			picture_dir = "user_img/"+username+"_profile.jpg"
			os.rename("tmp/"+key, picture_dir)
		else:
			picture_dir = "img/default.jpg"
		txt = ','.join(user.bleats)
		status = user.status
		conn = sqlite3.connect('database/User.db', timeout=10)
		c = conn.cursor()
		print username
		print type(username),type(full_name),type(email),type(listens),type(txt)
		sets = (username,full_name,email,listens,password,home_longitude,home_latitude,home_suburb,picture_dir,txt,status,)
		operation = '''INSERT INTO users values(null,?,?,?,?,?,?,?,?,?,?,?,0);'''
		c.execute(operation,sets)
		operation = '''DELETE FROM tmp_user WHERE key =?'''
		c.execute(operation,(user.UID,))
		conn.commit()
		c.close()
		conn.close()
		print Html.login_page_display()
	else:

		print """<div class='row'>
			<div class='col-xs-3' style='min-height:10em'></div>
				<div class='col-xs-6' style='padding-top:10em'>
					<h1 style='color:white;'> The key is expired or does not exist. </h1>
					<h1 style='color:white;'><a href='bitter.cgi'> Back to main page.</a> </h1>
				</div>
			</div>
		</div>"""
else:
	print Html.login_page_display()
print Html.footer()
