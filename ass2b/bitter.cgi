#!/usr/bin/python
import cgi, cgitb
import Classes
import fileSearchFunc
import Html,os,datetime
import Cookie,random
import sys, string, os, calendar, datetime, traceback
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

	dataset_size = "medium"

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
	except (Cookie.CookieError, KeyError):
	    cookie = Cookie.SimpleCookie()
	    cookie["logged_in"] =  0
	    expiration = datetime.datetime.now() + datetime.timedelta(seconds = 1000)
	    cookie["logged_in"]["expires"] = expiration
	    cookie_defined=False
	expiration = datetime.datetime.now() + datetime.timedelta(seconds = 1000)
	cookie["logged_in"]["expires"] = expiration
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
				log.write("\n57\n")
				print_string = print_string + Html.login_page_display(True,False,False)
			else:
				log.write("\n59\n")
				password = form['password'].value
				username = form['username'].value
				if password == "" or username == "":
					log.write("\n62\n")
					print_string = print_string +Html.login_page_display(True,False,False)
				else:
					log.write("\n66\n")
					user_file = fileSearchFunc.find_user_byID(dataset_size,username)
					if user_file == "":
						log.write("\n69\n")
						print_string = print_string + Html.login_page_display(False,True,False)
					else:
						log.write("\n72\n")
						# print "userfile",user_file
						user = Classes.User(dataset_size,user_file)
						# print user.password
						if not user.password == password:
							log.write("\n77\n")
							print_string = print_string + Html.login_page_display(False,False,True)
						else:
							log.write("\n80\n")
							cookie["logged_in"] = str(random.randrange(1, 10000000))
							log.write("\n82\n")
							cookie["username"] = username
							log.write("\n84\n")
							print_string = print_string + Html.nav_bar_display(username);
							log.write("\n86\n")
							user_display = Html.user_display(dataset_size,
								fileSearchFunc.find_user_byID(dataset_size,username))
							print_string = print_string + user_display.__str__()
							log.write("\n87\n")
		else:
			log.write("\n88\n")
			print_string = print_string + Html.login_page_display(False,False,False)
	else:
		if 'action' in form.keys():
			log.write("\n92\n"+cookie["logged_in"].value )
			action = form['action'].value
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
			elif action == "log_out":
				log.write("\n104\n")
				cookie["logged_in"] = 0
				print_string = print_string + Html.login_page_display(False,False,False)
			else:
				log.write("\n108\n")
				cookie["logged_in"] = 1
				print_string = print_string + Html.login_page_display(False,False,False)
		else:
			log.write("\n112\n")
			if "username" in cookie.keys():
				log.write("\n114\n")
				username = cookie["username"].value
				print_string = print_string + Html.nav_bar_display(username);
				user_display = Html.user_display(dataset_size,
					fileSearchFunc.find_user_byID(dataset_size,username))
				print_string = print_string + user_display.__str__()
			else:
				log.write("\n131\n")
				print_string = print_string + Html.login_page_display(False,False,False)
	log.write("\n123\n")
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
	msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
	arcpy.AddError(pymsg)
	arcpy.AddError(msgs)
	log.write("" + pymsg + "\n")
	log.write("" + msgs + "")
	log.close()