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


class div:
	def __init__(self,content = "",attributes=dict()):
		self.content = content
		self.attributes = attributes.copy()
		for k in self.attributes.keys():
			self.attributes[k] = list(self.attributes[k])
	def __str__(self):
		string="<div"
		for (k,v) in self.attributes.items():
			if type(v) == list or tuple:
				string+= " "+k+'="'+' '.join(v)+'"'
			else:
				string+= " "+k+'="'+v+'"'
		string+=">"+self.content+"</div>"
		return string
	def add(self,attr,prop):
		if attr in self.attributes.keys():
			self.attributes[attr].append(prop)
		else:
			self.attributes[attr]=list(prop)
	def delete(self,attr,prop):
		if attr in self.attributes:
			if prop in self.attributes[attr]:
				self.attributes[attr].remove(prop)
				if len(self.attributes[attr]) == 0:
					del self.attributes[attr]
