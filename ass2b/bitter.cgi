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
print_string =  print_string + Html.header("Bitter").__str__()
if not login_validate.validate(cookie["logged_in"].value):
	if 'action' in form.keys():
		action = form['action'].value
	else:
		action = ""
	if action == 'Login':
		if not 'password' in form.keys() or not 'username' in form.keys():
			print_string = print_string + Html.login_page_display(empty = True)
		else:
			password = form['password'].value
			username = form['username'].value
			if password == "" or username == "":
				print_string = print_string +Html.login_page_display(empty = True)
			else:
				user = Search.search_user_by_ID_e(username)
				if user.exist == False:
					print_string = print_string + Html.login_page_display ( not_exist = True)
				else:
					if not user.password == password:
						print_string = print_string + Html.login_page_display(wrong = True)
					else:
						cookie["logged_in"] = str(random.randrange(1, 10000000))
						cookie["username"] = username
						user.main_page()
						print_string = print_string + Html.nav_bar_display(username)
						print_string = print_string + user.user_display()
	elif action == 'Register':
		print_string += Html.register_page()
	else:
		print_string = print_string + Html.login_page_display()
else:
	if 'action' in form.keys():
		action = form['action'].value
		if action == "User_name":
			username = form['username'].value
			user = Search.search_user_by_ID_e(username)
			print_string = print_string + Html.nav_bar_display(username)
			print_string = print_string + user.user_display()
		elif action == "un_listen":
			me = cookie["username"].value
			username = form['username'].value
			user = Search.search_user_by_ID_e(me)
			try:
				user.listens.remove(username)
			except:
				pass
			user.update()
			print_string = print_string + Html.nav_bar_display(username)
			print_string = print_string + user.user_display()
		elif action == "listen":
			me = cookie["username"].value
			username = form['username'].value
			user = Search.search_user_by_ID_e(me)
			try:
				if not username in user.listens and not username == me:
					user.listens.append(username)
			except:
				pass
			user.update()
			print_string = print_string + Html.nav_bar_display(username)
			print_string = print_string + user.user_display()
		elif action == "main":
			username = cookie["username"].value
			print_string = print_string + Html.nav_bar_display(username)
			user = Search.search_user_by_ID_e(username)
			user.main_page()
			print_string = print_string + user.user_display()
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
print_string = cookie.output() +"\n\n"+ print_string + Html.footer().__str__()
print print_string
