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

form = cgi.FieldStorage()
if 'action' in form.keys():
	action = form['action'].value
else:
	action = ""
if action == "register":
	print "HI"
	username=form["username"].value
	if Search.search_user_by_ID_e(username).exist:
		print "<h2>The user name already exists!!!!</h2>"
		print Html.footer()
	else:
		# generate a random key
		random_key = str(random.randrange(1, 10000000))
		# make the form into the temperory cached user
		if 'file' in form.keys():
			# A nested FieldStorage instance holds the file
			fileitem = form['file']

			# Test if the file was uploaded
			if fileitem.filename:
	   			# strip leading path from file name to avoid directory traversal attacks
				fn = os.path.basename(random_key)
				tmp_path = 'tmp/'+fn
				open('tmp/'+fn, 'w').write(fileitem.file.read())
			else:
				tmp_path=""
		else:
			tmp_path=""

		password=form["password"].value
		full_name=form["full_name"].value
		email=form["email"].value
		try:
			longitude = form["longitude"].value
		except:
			longitude = 0
		try:
			latitude = form["latitude"].value
		except:
			latitude = 0
		try:
			suburb = form["suburb"].value
		except:
			suburb = ""
		try:
			status = special_char_filter.special_char_filter(form["self_intro"].value) 
		except:
			status = ""
		conn = sqlite3.connect('database/User.db')
		c = conn.cursor()
		sets = (int(random_key),username,full_name,email,"",password,longitude,latitude,suburb,tmp_path,"",status)
		operation = '''INSERT INTO tmp_user values(?,?,?,?,?,?,?,?,?,?,?,?,0);'''
		c.execute(operation,sets)
		conn.commit()
		conn.close()

		# generate the coresponding key link
		address = os.environ["SCRIPT_URI"]
		link= re.sub("/register.cgi","/register_verify.cgi?key="+random_key,address)
		print link
		# send email to the target email
		# 
		# import subprocess
		print "<h2> verifying email has been sent to your mailbox of :"+ email+"<p/> Please click through the link to activate your account.</h2>"
		# import smtplib

		# sender = 'bitter.auto@bitter.com'
		# receivers = ['markshen5295@gmail.com']

		# message = """From: From Person <bitter.auto@bitter.com>
		# To:  <{1}>
		# Subject: Verify your registration

		# Click through this link : {0}
		# """.format(link,email)

		# smtpObj = smtplib.SMTP('localhost')
		# # smtpObj.login('comp2041ass2ms@gmail.com','12345qazwsx')
		# smtpObj.sendmail(sender, receivers, message)   

		pass
else:
	print Html.login_page_display(False,False,False)
print Html.footer()