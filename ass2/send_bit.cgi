#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html,re
import Search,login_validate
import special_char_filter
import sqlite3
print "Content-Type: text/html"
base = "html/"
img_base = 'bleat_img/'
default_str=""
bleat_database = 'database/Bleats.db'
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
				in_reply_to = default_str
			try:
				latitude = form["latitude"].value
			except:
				latitude = default_str
			try:
				longitude = form["longitude"].value
			except:
				longitude = default_str
			
			video = default_str
			# Get the time
			import datetime
			dt = (datetime.datetime.now()-datetime.datetime(1970,1,1))
			time = dt.days * 1440*60 + dt.seconds
			# Upload pic items
			pic_list = list()
			if "myPic" in form.keys():
				fileitems = form["myPic"]
				i=0
				# Avoid fileitem to be only one or empty
				if not isinstance(fileitems,list):
					fileitems = [fileitems]
				for fileitem in fileitems:
					if fileitem.filename:
			   			# naming principle of the picture: username+"_"+timestamp+"_"+pic_No+.whatever
			   			file_type = re.sub(r'^.*(\.[^\.]*)$',r'\1',fileitem.filename)
			   			fn = username+"_"+str(time)+"_"+str(i)+file_type
						pic_path = img_base+os.path.basename(fn)
						open(pic_path, 'w').write(fileitem.file.read())
						pic_list.append(pic_path)
						i+=1
						
			picture = ", ".join(pic_list)
			# Update the bleats database
			conn = sqlite3.connect(bleat_database)
			c = conn.cursor()
			data = (username,content,in_reply_to,time,longitude,latitude,default_str,picture,video)
			c.execute( 'INSERT INTO bleats VALUES(null,?,?,?,?,?,?,?,?,?);',data)
			conn.commit()
			c.close()
			conn.close()
			
			# Get the bleatID
			conn = sqlite3.connect(bleat_database)
			c = conn.cursor()
			operation="SELECT bleatID FROM bleats WHERE username = ? AND bleat = ? AND time = ?;"
			selection=(username,content,time)
			c.execute(operation,selection)
			bleatID = str(c.fetchone()[0])
			c.close()
			conn.close()
			
			# Print the user's page
			user = Search.search_user_by_ID_e(username)
			print user.user_display()
			# Send email to related person
			import smtplib
			sender = 'comp2041ass2ms@gmail.com'
			smtpObj = smtplib.SMTP('smtp.gmail.com:587')
			smtpObj.starttls()
			smtpObj.login(sender,'12345qazwsx')
			if not in_reply_to == "":
				bleat_r = Search.search_bleat_by_bleat_ID(in_reply_to)
				user = Search.search_user_by_ID_e(bleat_r.author)
				email = user.email
				receivers = email
				
				message = """From: Bitter authority <bitter.auto@bitter.com>
				To:  <{1}>
				Subject: {2} Replied you
				
				{2} replied your bleat: {0}
				Saying that:
				{3}
				""".format(bleat_r.content,email,username,content)
				smtpObj.sendmail(sender, receivers, message)
				
				#update the mentioned by
				mentioned = Search.search_notification_by_username(user.username)
				mentioned.add_mentioned(bleatID)
				mentioned.update()
			for mentioned in re.findall(r'@\w+',content):
				user = Search.search_user_by_ID_e(mentioned[1:])
				if user.exist:
					email = user.email
					receivers = email
					message = """From: Bitter authority <bitter.auto@bitter.com>
					To:  <{1}>
					Subject: {2} Mentioned you
				
					{2} mentioned you in the bleat: {0}
					""".format(content,email,username)
					smtpObj.sendmail(sender, receivers, message)
					mentioned = Search.search_notification_by_username(user.username)
					mentioned.add_mentioned(bleatID)
					mentioned.update()
			smtpObj.quit()
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
