#!/usr/bin/python
import cgi, cgitb
import os,datetime
import Cookie,random,time, datetime
#import own library
import Search,Html
import login_validate

cgitb.enable(display=0, logdir="/logdir")
form = cgi.FieldStorage()
print_string = ""
#start of main function
# Required header that tells the browser how to render the text.
print "Content-Type: text/html"
try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cookie["logged_in"]
except (Cookie.CookieError, KeyError):
    cookie = Cookie.SimpleCookie()
    cookie["logged_in"] =  0
    expiration = datetime.datetime.now() + datetime.timedelta(seconds = 1000)
    cookie["logged_in"]["expires"] = 20
    cookie["logged_in"]["max-age"] = 50

# Add the header of the html
print_string =  print_string + Html.header("Bitter").__str__()

# If not logged in
if not login_validate.validate(cookie["logged_in"].value):
	if 'action' in form.keys():
		action = form['action'].value
	else:
		action = ""
	# Login verification
	if action == 'Login':
		# Password or username missing
		if not 'password' in form.keys() or not 'username' in form.keys():
			print_string = print_string + Html.login_page_display(empty = True)
		else:
			password = form['password'].value
			username = form['username'].value
			
			# Password or username missing
			if password == "" or username == "":
				print_string = print_string +Html.login_page_display(empty = True)
			else:
				user = Search.search_user_by_ID_e(username)
				# if the user doesn't even exist
				if user.exist == False:
					print_string = print_string + Html.login_page_display ( not_exist = True)
				else:
					# Wrong password
					if not user.password == password:
						print_string = print_string + Html.login_page_display(wrong = True)
					# login success!!!
					else:
						cookie["logged_in"] = str(random.randrange(1, 10000000))
						cookie["username"] = username
						user.main_page()
						print_string = print_string + Html.nav_bar_display(username)
						print_string = print_string + user.user_display()
	# Print the register page
	elif action == 'Register':
		print_string += Html.register_page()
	# Print the login page
	else:
		print_string = print_string + Html.login_page_display()

# If logged in
else:
	if 'action' in form.keys():
		action = form['action'].value
		# View a specific user
		if action == "User_name":
			me = cookie["username"].value
			username = form['username'].value
			user = Search.search_user_by_ID_e(username)
			print_string = print_string + Html.nav_bar_display(me)
			print_string = print_string + user.user_display()
		# Unlisten a user
		elif action == "un_listen":
			me = cookie["username"].value
			username = form['username'].value
			user = Search.search_user_by_ID_e(me)
			try:
				user.listens.remove(username)
			except:
				pass
			user.update()
			print_string = print_string + Html.nav_bar_display(me)
			print_string = print_string + user.user_display()
		# Start listening to a user
		elif action == "listen":
			me = cookie["username"].value
			username = form['username'].value
			user = Search.search_user_by_ID_e(me)
			try:
				if not username in user.listens and not username == me:
					user.listens.append(username)
					user_l = Search.search_user_by_ID_e(username)
					email = user_l.email

					# send email
					import smtplib

					sender = 'comp2041ass2ms@gmail.com'
					receivers = email

					message = """From: From Person <bitter.auto@bitter.com>
					To:  <{1}>
					Subject: {0} starts listening to you now!
					{0} starts listening to you now!
					""".format(me,email)

					smtpObj = smtplib.SMTP('smtp.gmail.com:587')
					smtpObj.starttls()
					smtpObj.login(sender,'12345qazwsx')
					smtpObj.sendmail(sender, receivers, message)  
					smtpObj.quit() 
			except:
				pass
			user.update()
			print_string = print_string + Html.nav_bar_display(me)
			print_string = print_string + user.user_display()
			mentioned = Search.search_notification_by_username(username)
			mentioned.add_listen(me)
			mentioned.update()
		
		# Display the main page of the user ( including the bleat from people he is listening to)
		elif action == "main":
			username = cookie["username"].value
			print_string = print_string + Html.nav_bar_display(username)
			user = Search.search_user_by_ID_e(username)
			user.main_page()
			print_string = print_string + user.user_display()
		
		# Log out
		elif action == "log_out":
			cookie["logged_in"] = 0
			print_string = print_string + Html.login_page_display(False,False,False)
		else:
			print_string = print_string + Html.login_page_display(False,False,False)
	else:
		if "username" in cookie.keys():
			username = cookie["username"].value
			user = Search.search_user_by_ID_e(username)
			print_string = print_string + Html.nav_bar_display(username)
			user.main_page()
			print_string = print_string + user.user_display()
		else:
			print_string = print_string + Html.login_page_display(False,False,False)
# Print the cookie
print_string = cookie.output() +"\n\n"+ print_string + Html.footer().__str__()
# print the rest of the html
print print_string
