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
		if 'key_word' in form.keys():
			key = form['key_word'].value
			key = special_char_filter.special_char_filter(key)
			bleat_list = Search.search_bleat_by_content(key)
			if len(bleat_list) > 0:
				string=""
				for bleat in bleat_list:
					string+= bleat.format_bleat()
				print "<div class='offset3 col-xs-12 col-sm-8 col-md-6'>"
				print open(base+"bleat_panel.html").read().format(string)
				print open(base+"style_bleat.html").read()
				print "</div>"
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
