#!/usr/bin/python

###############################################
## Html library written by Minjie Shen       ##
## including basic tags that might be used   ##
## in html and can set attributes to them.   ##
###############################################

import Classes
from Classes import User
from Classes import Bleat
#some globals
base = "html/"



# this is the generic class of a tag		
class tag:
	def __init__(self,name,content = "",attributes=dict()):
		self.name = name
		self.content = content
		self.attributes = attributes.copy()
		for k in self.attributes.keys():
			self.attributes[k] = [self.attributes[k]]
		# print self
	def __str__(self):
		string="<"+self.name
		for (k,v) in self.attributes.items():
			if type(v) == list:
				string+= " "+k+'="'+' '.join(v)+'"'
			else:
				string+= " "+k+'="'+v+'"'
		string+=">"+self.content+"</"+self.name+">"
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

#commonly used tags
class div(tag):
	def __init__(self,content = "",attributes=dict()):
		tag.__init__(self,"div",content,attributes)

class a(tag):
	def __init__(self,href,content = "",attributes=dict()):
		attributes["href"]=href
		tag.__init__(self,"a",content,attributes)

class img(tag):
	def __init__(self,src,content = "",attributes=dict()):
		attributes["src"]=src
		tag.__init__(self,"img",content,attributes)

# html templates
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

#These are temporary
class user_info(User):
	def __init__(self,dataset_size,userdir):
		User.__init__(self,dataset_size,userdir)
	def __str__(self):
		return self.user_info()
	def user_info(self):
		return '''	    <div class="thumbnail">
	      {0}
	      <div class="caption">
		<h3>{1}</h3>
		<pre>{2}</pre>
		<p>
	      </div>
	    </div>'''.format(img(self.pic_path).__str__(),,)


class listening(User):
	def __init__(self,dataset_size,userdir):
		self.listening = User(dataset_size,userdir).listens
	def __str__(self):
		return self.pic_path
	def print_listening(self):
		string='''<div class="list-group">
	  				<div class="list-group-item active">
	  					Listening
	  				</div>
				'''
		for listen in self.listening:
			string +='''<form action="" method="post" class="list-group-item user-listen">
				<input type="hidden" name="username" value="{0}">
				<button value="User_name" name="action" class="list-group-item">{0}</button>
			</form>
			'''.format(listen)
		string += "\n</div>"
		return string
class bleats(Bleat):
	def __init__(self,dataset_size,num_list=list()):
		self.list = list()
		self.list = [Bleat(dataset_size,n) for n in num_list]
	def print_bleats(self):
		return "bleats"

class user_display(user_info,bleats,listening):
	def __init__(self,dataset_size,userdir):
		user_info.__init__(self,dataset_size,userdir)
		num_list=self.bleat_list()
		bleats.__init__(self,dataset_size,num_list)
		listening.__init__(self,dataset_size,userdir)
	def __str__(self):
		txt = open(base + "user_display.html").read()
		return txt.format(self.user_info(),
			self.print_listening(),self.print_bleats())

def login_page_display(empty=False,exist=False,wrong=False):
	em="hidden"
	ex="hidden"
	wr="hidden"
	if empty:
		em=""
	elif exist:
		ex=""
	elif wrong:
		wr=""
	string = open(base + "login.html",'r').read().format("img/You-Shall-Not-Pass.png",
				em,ex,wr)
	return string + open(base+"style.html",'r').read()