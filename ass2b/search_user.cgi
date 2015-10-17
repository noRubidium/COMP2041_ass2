#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
import Search,login_validate
print "Content-Type: text/html"
base = "html/"
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	if login_validate.validate(cookie["logged_in"].value):
		print cookie.output()
		print
		print Html.header("Bitter")
		username = cookie["username"].value
		print Html.nav_bar_display(username)
		form = cgi.FieldStorage()
		if 'username' in form.keys():
			username_s = form['username'].value
			uList_1 = Search.search_user_by_ID_a(username_s)
			uList_2 = Search.search_user_by_full_name(username_s)
			uList_1+=uList_2
			string=""
			for user in uList_1:
				try:
					bleatNo = user.bleats[-1]
					bleat = Search.search_bleat_by_bleat_ID(bleatNo)
					bleat = bleat.content
				except:
					bleat = "This user doesn't have recent bleats."
				string+=open(base+"user_short.html").read().format(user.username, user.full_name,Html.img(user.pic_path).__str__(),bleat)
			print open(base+"user_search.html").read().format(string,username_s)
			print open(base+"page.html").read()
		else:
			#print the default empty search page
			print open(base+"404.html").read()
		print Html.footer()
	else:
		print 
		print
		print Html.header("Bitter")
		print Html.login_page_display()
		print Html.footer()
except (Cookie.CookieError, KeyError):
	print 
	print
	print Html.header("Bitter")
	print Html.login_page_display()
	print Html.footer()
