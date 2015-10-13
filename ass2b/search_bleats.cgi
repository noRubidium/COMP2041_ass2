#!/usr/bin/python
import cgi, cgitb
import Cookie,os
import Html
import Search,login_validate
import special_char_filter
import sqlite3
print "Content-Type: text/html"
base = "html/"

