#!/usr/bin/python
import cgi, cgitb
import Classes
import fileSearchFunc
import Html
# from Classes import User
#start of all types of helper function


dataset_size = "medium"
# users_dir = "dataset-"+dataset_size+"/users"
# bleats_dir = "dataset-"+dataset_size+"/bleats"

# cgitb.enable()
form = cgi.FieldStorage()

#start of main function
# Required header that tells the browser how to render the text.
print "Content-Type: text/html\n\n"
print Html.header("Bitter")
if 'action' in form.keys():
	action = form['action'].value
	print action
	if action == "Login":
		if not 'password' in form.keys() or not 'username' in form.keys():
			print Html.login_page_display(True,False,False)
		else:
			password = form['password'].value
			username = form['username'].value

			if password == "" or username == "":
				print Html.login_page_display(True,False,False)
			else:
				user_file = fileSearchFunc.find_user_byID(dataset_size,username)
				if user_file == "":
					print Html.login_page_display(False,True,False)
				else:
					# print "userfile",user_file
					user = Classes.User(dataset_size,user_file)
					# print user.password
					if not user.password == password:
						print Html.login_page_display(False,False,True)
					else:
						user_display = Html.user_display(dataset_size,
							fileSearchFunc.find_user_byID(dataset_size,username))
						print user_display
	elif action == "User_name":
		username = form['username'].value
		user_file = fileSearchFunc.find_user_byID(dataset_size,username)
		user_display = Html.user_display(dataset_size,
			fileSearchFunc.find_user_byID(dataset_size,username))
		print user_display
	elif action == "search_user":
		pass
else:
	# Not yet logged in (for now)
	print Html.login_page_display(False,False,False)

print Html.footer()