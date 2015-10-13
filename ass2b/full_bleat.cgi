#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
import Search,login_validate
import special_char_filter
print "Content-Type: text/html"
base = "html/"
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	if login_validate.validate(cookie["logged_in"].value):
		print cookie.output()
		print
		print Html.header("Bitter").__str__()
		username = cookie["username"].value
		print Html.nav_bar_display(username)
		form = cgi.FieldStorage()
		if "bleat_No" in form.keys():
			bleat_No = form["bleat_No"].value
			bleat = Search.search_bleat_by_bleat_ID(bleat_No)
			if bleat.exist:
				author = Search.search_user_by_ID_e(bleat.author);
				string = author.user_info()
				print open(base+"full_bleat.html").read().format(bleat.print_loc_row(),
		bleat.print_reply(),bleat.format_content(),bleat.author,bleat.time,bleat.bleat_No,string)
				print open(base+"style_bleat.html").read()
			else:
				print open(base+"404.html").read()
		else:
			#print the default empty search page
			print open(base+"404.html").read()
		print Html.footer().__str__()
	else:
		print 
		print
		print Html.header("Bitter").__str__()
		print Html.login_page_display()
		print Html.footer().__str__()
except (Cookie.CookieError, KeyError):
	print 
	print
	print Html.header("Bitter").__str__()
	print Html.login_page_display()
	print Html.footer().__str__()
