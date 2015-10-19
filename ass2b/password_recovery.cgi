#!/usr/bin/python
import cgi, cgitb
import Html,Search
import sqlite3,os
import random,re
import special_char_filter

import cgitb
cgitb.enable()

default_str = ""
print "Content-Type: text/html"
print
print
print Html.header("Bitter")
base="html/"

form = cgi.FieldStorage()
if 'action' in form.keys():
	action = form['action'].value
else:
	action = ""
if action == "send_email":
	if 'username' in form.keys() and 'email' in form.keys():
		username = form['username'].value
		email = form['email'].value
		user = Search.search_user_by_ID_e(username)
		if user.exist and user.email == email:
			key = str(random.randrange(1, 10000000))
			# Generate the varify address
			conn = sqlite3.connect("database/User.db")
			c = conn.cursor()
			operation = "INSERT INTO forgot_password VALUES(?,?,?);"
			setting = (key,email,user.password)
			c.execute(operation,setting)
			conn.commit()
			conn.close()
			address = os.environ["SCRIPT_URI"]
			link = address+"?action=verify&key="+key
			# send email
			import smtplib

			sender = 'comp2041ass2ms@gmail.com'
			receivers = email

			message = """From: From Person <bitter.auto@bitter.com>
			To:  <{1}>
			Subject: Verify your registration

			Click through this link : {0}
			""".format(link,email)

			smtpObj = smtplib.SMTP('smtp.gmail.com:587')
			smtpObj.starttls()
			smtpObj.login(sender,'12345qazwsx')
			smtpObj.sendmail(sender, receivers, message)  
			smtpObj.quit() 
			# print page
			print "<h2> The email has been sent to your email address please check. <a href='bitter.cgi'>Back to front page </a></h2>"
			print link
		else:
			print '''<div class="col-xs-6 alert alert-warning alert-dismissible" style="z-index:5;position:absolute;top:50%;left:50%;margin:-25% -25%" role="alert">
				  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
				  <strong>Warning!</strong> The email address or the username is wrong, please try again.
				</div>'''
			print open(base+"password_recovery.html").read()

	else:
		print open(base+"password_recovery.html").read()
elif action == "verify":
	try:
		key=form['key'].value
		conn = sqlite3.connect("database/User.db")
		c = conn.cursor()
		print "HI!!"
		c.execute("SELECT * FROM forgot_password WHERE key = ?;",(key,))
		
		w = c.fetchone()
		print "<h2>Your password is: "+w[2]+" </h2>"
		c.execute("DELETE FROM forgot_password WHERE key = ?;",(key,))
		conn.commit()
		conn.close()
		print "<h2><a href='bitter.cgi'>Back to front page </a></h2>"
	except:
		print '''<div class="col-xs-6 alert alert-warning alert-dismissible" style="z-index:5;position:absolute;top:50%;left:50%;margin:0 -25%" role="alert">
				  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
				  <strong>Warning!</strong> The key is expired please try again.
				</div>'''
		print open(base+"password_recovery.html").read()
else:
	print open(base+"password_recovery.html").read()
print Html.footer()
