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
# Required header that tells the browser how to render the text.
# os.path.isfile(fname) 
# user_file = fileSearchFunc.find_user_byID(dataset_size,"Vitali86")
# #print username
# if user_file == "":
# 	print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
# 		"hidden","","hidden")
# 	print open("style.html",'r').read()
# else:
# 	print "Userfile",user_file
# 	user = Classes.User(dataset_size,user_file)
# 	if not user.password == password:
# 		print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
# 			"hidden","","hidden")
# 		print open("style.html",'r').read()
# 	else:
# 		print "<p>Login Success!!!</p>"
# fileSearchFunc.find_user_byID(dataset_size,"DSAF")

#start of main function
print "Content-Type: text/html\n\n"
print Html.header("Bitter")
if 'action' in form.keys():
	action = form['action'].value
	if action == "Login":
		if not 'password' in form.keys() or not 'username' in form.keys():
			print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
				"","hidden","hidden")
			print open("style.html",'r').read()
		else:
			password = form['password'].value
			username = form['username'].value
			user_file = fileSearchFunc.find_user_byID(dataset_size,username)
			#print username
			
			if user_file == "":
				print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
					"hidden","","hidden")
				print open("style.html",'r').read()
			else:
				print "userfile",user_file
				user = Classes.User(dataset_size,user_file)
				print user.password
				if not user.password == password:
					print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
						"hidden","hidden","")
					print open("style.html",'r').read()
				else:
					print "<p>Login Success!!!</p>"

else:
	print open("login.html",'r').read().format("img/You-Shall-Not-Pass.png",
		"hidden","hidden","hidden")
	print open("style.html",'r').read()
# userfiles = fileSearchFunc.find_user(dataset_size,"a")
# for filename in userfiles:
# 	user = Html.user_display(dataset_size,filename)
# 	# # print user.print_bleats()
# 	# bleat = Classes.Bleat(dataset_size,user.bleats[0])
# 	print user
# 	print "<p/>"
# div = Html.div("Hi",{"class":("nav","l")})
# div.delete("class","l")
# div.delete("class","nav")
# print div

print Html.footer()