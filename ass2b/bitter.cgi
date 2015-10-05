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



#start of main function
print "Content-Type: text/html\n\n"
print Html.header("user")
userfiles = fileSearchFunc.find_user(dataset_size,"a")
for filename in userfiles:
	user = Classes.User(dataset_size,filename)
	# print user.print_bleats()
	bleat = Classes.Bleat(dataset_size,user.bleats[0])
	print bleat
	print "<p/>"
print Html.footer()