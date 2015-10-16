#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cookie["logged_in"] = 0
    print "Content-Type: text/html"
    print cookie.output()
    print
    print Html.header("Bitter")
    print Html.login_page_display()
    print Html.footer()
except (Cookie.CookieError, KeyError):
    print "Content-Type: text/html"
    print 
    print
    print Html.header("Bitter")
    print Html.login_page_display()
    print Html.footer()