#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html,re
import Search,login_validate
print "Content-Type: text/html"
base = "html/"

try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	form = cgi.FieldStorage()
	if login_validate.validate(cookie["logged_in"].value):
		username = cookie["username"].value
		user = Search.search_user_by_ID_e(username)
		if user.exist:
			print cookie.output()
			print
			print Html.header("Bitter")	
			print Html.nav_bar_display(username)	
			recommend_list = user.listens
			recommend_list.append(username)
			string = ""
			print open(base+"page.html").read()
			print """<div class="col-xs-3"></div><div class="col-xs-6" align="center">
			<div class="list-group-item active">
				<h1>
				People you may know
				</h1>
			</div>"""
			for listen in user.listens:
				curr = Search.search_user_by_ID_e(listen)
				for username_curr in curr.listens:
					if not username_curr in recommend_list:
						recommend_list.append(username_curr)
						curr_user = Search.search_user_by_ID_e(username_curr)
						try:
							bleatNo = curr_user.bleats[-1]
							bleat = Search.search_bleat_by_bleat_ID(bleatNo)
							bleat = bleat.content
						except:
							bleat = "This user doesn't have recent bleats."
						print open(base+"user_short.html").read().format(curr_user.username, 
						curr_user.full_name,Html.img(curr_user.pic_path).__str__(),bleat)	
			print '''<div id="user_page" class="list-group-item"></div></div>'''
			
		else:
			print 
			print 
			print Html.header("Bitter").__str__()
			print Html.login_page_display()
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
