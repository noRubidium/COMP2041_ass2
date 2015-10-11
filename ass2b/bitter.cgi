#!/usr/bin/python
import cgi, cgitb
import os,datetime
import Cookie,random,time, datetime
#import lib for debugging
import sys, string, os, calendar, traceback
#import own library
import Search,Html
import login_validate
try:
	#debugging and log writing statement starts
	d = datetime.datetime.now()
	log = open("PythonOutputLogFile.txt","a")
	log.write("----------------------------" + "\n")
	log.write("----------------------------" + "\n")
	log.write("Log: " + str(d) + "\n")
	log.write("\n")
	starttime = datetime.datetime.now()
	log.write("Begin process:\n")
	log.write("     Process started at " 
	   + str(starttime) + "\n")
	log.write("\n")

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
	log.write("COOKIE_TIME:"+str(cookie["logged_in"]["expires"]))
	print_string =  print_string + Html.header("Bitter").__str__()
	if not login_validate.validate(cookie["logged_in"].value):
		if 'action' in form.keys():
			action = form['action'].value
			print_string += action
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
						print_string = print_string + Html.login_page_display(not_exist = True)
					else:
						if not user.password == password:
							print_string = print_string + Html.login_page_display(wrong = True)
						else:
							cookie["logged_in"] = str(random.randrange(1, 10000000))
							cookie["username"] = username
							print_string = print_string + Html.nav_bar_display(username);
							print_string = print_string + user.user_display()
		else:
			print_string = print_string + Html.login_page_display()
	else:
		if 'action' in form.keys():
			action = form['action'].value
			log.write("\nACTION:"+action+"\n")
			if action == "User_name":
				username = form['username'].value
				user = Search.search_user_by_ID_e(username)
				print_string = print_string + Html.nav_bar_display(username)
				print_string = print_string + user.user_display()
			elif action == "main":
				username = cookie["username"].value
				user = Search.search_user_by_ID_e(username)
				print_string = print_string + Html.nav_bar_display(username)
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
				print_string = print_string + user.user_display()
			else:
				print_string = print_string + Html.login_page_display(False,False,False)
	print_string = cookie.output() +"\n\n"+ print_string + Html.footer().__str__()
	print print_string
	endtime = datetime.datetime.now()
	log.write("     Completed successfully in " + str(endtime - starttime) + "\n")
	log.write("\n")
	log.close()
except:
	tb = sys.exc_info()[2]
 	tbinfo = traceback.format_tb(tb)[0]
 	pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
	log.write("" + pymsg + "\n")
	log.write("Line number:"+str(sys.exc_traceback.tb_lineno) +"\n")
	log.close()
