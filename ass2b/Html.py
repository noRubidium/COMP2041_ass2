#!/usr/bin/python

###############################################
## Html library written by Minjie Shen       ##
## including basic tags that might be used   ##
## in html and can set attributes to them.   ##
###############################################
base = "html/"
class header:
	def __init__(self,title=""):
		self.title = title
	def __str__(self):
		txt = open(base + "header.html").read()
		return txt.format(self.title)
class footer:
	def __init__(self):
		self.content = open(base + "footer.html").read()
	def __str__(self):
		return self.content