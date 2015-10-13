#!/usr/bin/python
import cgi, cgitb
import Classes
import fileSearchFunc
import Html,os,datetime
import Cookie,random,time, datetime
import sys, string, os, calendar, traceback
try:
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

	dataset_size = "large"

	cgitb.enable(display=0, logdir="/logdir")
	form = cgi.FieldStorage()
	print_string = ""
	#start of main function
	# Required header that tells the browser how to render the text.
	print "Content-Type: text/html"

	try:
	    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	    cookie["logged_in"]
	    cookie_defined = True
	    log.write("\nsuccessfully Completed line 35\n")
	except (Cookie.CookieError, KeyError):
	    cookie = Cookie.SimpleCookie()
	    cookie["logged_in"] =  0
	    expiration = datetime.datetime.now() + datetime.timedelta(seconds = 1000)
	    cookie["logged_in"]["expires"] = 20
	    cookie["logged_in"]["max-age"] = 50
	    cookie_defined=False
	log.write("COOKIE_TIME:"+str(cookie["logged_in"]["expires"]))
	print_string =  print_string + Html.header("Bitter").__str__()
	log.write(print_string)
	log.write("\nsuccessfully Completed line 45\n")
	if  cookie["logged_in"].value == '0' :
		if 'action' in form.keys():
			log.write("\n50\n")
			action = form['action'].value
			print_string += action
		else:
			log.write("\n52\n")
			action = ""
		if action == 'Login':
			if not 'password' in form.keys() or not 'username' in form.keys():
				print_string = print_string + Html.login_page_display(True,False,False)
			else:
				password = form['password'].value
				username = form['username'].value
				if password == "" or username == "":
					print_string = print_string +Html.login_page_display(True,False,False)
				else:
					user_file = fileSearchFunc.find_user_byID(dataset_size,username)
					if user_file == "":
						print_string = print_string + Html.login_page_display(False,True,False)
					else:
						# print "userfile",user_file
						user = Classes.User(dataset_size,user_file)
						# print user.password
						if not user.password == password:
							print_string = print_string + Html.login_page_display(False,False,True)
						else:
							cookie["logged_in"] = str(random.randrange(1, 10000000))
							cookie["username"] = username
							print_string = print_string + Html.nav_bar_display(username);
							user_display = Html.user_display(dataset_size,
								fileSearchFunc.find_user_byID(dataset_size,username))
							print_string = print_string + user_display.__str__()
		else:
			print_string = print_string + Html.login_page_display(False,False,False)
	else:
		if 'action' in form.keys():
			action = form['action'].value
			log.write("\nACTION:"+action+"\n")
			if action == "User_name":
				log.write("\n94\n")
				username = form['username'].value
				print_string = print_string + Html.nav_bar_display(username);
				user_file = fileSearchFunc.find_user_byID(dataset_size,username)
				user_display = Html.user_display(dataset_size,
					fileSearchFunc.find_user_byID(dataset_size,username))
				print_string = print_string + user_display.__str__()
			elif action == "search_user":
				pass
			elif action == "main":
				username = cookie["username"].value
				print_string = print_string + Html.nav_bar_display(username);
				user_display = Html.user_display(dataset_size,
					fileSearchFunc.find_user_byID(dataset_size,username))
				print_string = print_string + user_display.__str__()
			elif action == "log_out":
				cookie["logged_in"] = 0
				print_string = print_string + Html.login_page_display(False,False,False)
			else:
				print_string = print_string + Html.login_page_display(False,False,False)
		else:
			if "username" in cookie.keys():
				username = cookie["username"].value
				print_string = print_string + Html.nav_bar_display(username);
				user_display = Html.user_display(dataset_size,
					fileSearchFunc.find_user_byID(dataset_size,username))
				print_string = print_string + user_display.__str__()
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
	# msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
	# arcpy.AddError(pymsg)
	# arcpy.AddError(msgs)
	log.write("" + pymsg + "\n")
	# log.write("" + msgs + "")
	log.close()