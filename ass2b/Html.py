#!/usr/bin/python

###############################################
## Html library written by Minjie Shen       ##
## including basic tags that might be used   ##
## in html and can set attributes to them.   ##
###############################################

import glob, re
import os.path
import datetime
import sqlite3
import cgi

# This section define some global variables
default_str = ""
bleat_error = "This bleat unavailable (has been deleted or not wrong reference)."
user_not_exist = "This user does not exist in the data base!"
base = "html/"

# definition of all types of classes

# cgi.test()
# this is the generic class of a tag		
class tag:
	def __init__(self,name,content = "",attributes=dict()):
		self.name = name
		self.content = content
		self.attributes = attributes.copy()
		for k in self.attributes.keys():
			self.attributes[k] = [self.attributes[k]]
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

# location can be used to store location and calculate the distance and many things
# it's one of the super classes
class Location(object):
	def __init__(self,longitude=default_str,latitude=default_str,suburb=default_str):
		self.longitude = longitude
		self.latitude = latitude
		self.suburb = suburb
	def __str__(self):
		return self.print_loc_row()
	def print_loc_row(self):
		return open(base+"loc_row.html").read().format(self.longitude,self.latitude)
	def get_long(self):
		return open(base+"loc_long.html").read().format(self.longitude,"Longitude: ")
	def get_lat(self):
		return open(base+"loc_long.html").read().format(self.latitude,"Latitude: ")
	def get_sub(self):
		return open(base+"loc_long.html").read().format(self.suburb,"Suburb: ")
	def print_loc(self):
		return self.get_long()+self.get_lat() +self.get_sub()

# Picture class can be used to store the user's photo location 
# and may print the photo in a nicely formated 
class Picture(object):
	def __init__(self,picdir):
		self.pic_path = picdir
	def __str__(self):
		return img(self.pic_path).__str__()
		


# Bleat class can be used to store the bleats
class Bleat(Location):
	def __init__(self,bleat_No=default_str,username=default_str, content=default_str,in_reply_to=default_str,
	time=default_str,longitude=default_str,latitude=default_str,is_exist=True):
			self.bleat_No=bleat_No
			Location.__init__(self,longitude,latitude)
			self.content = content
			if time == default_str:
				time = "0"
			time = datetime.datetime(1970,1,1) + datetime.timedelta(0,int(time))
			self.time = time
			self.author = username
			self.in_reply_to = in_reply_to
			self.exist = is_exist
	def format_content(self):
		result = self.content
		result = re.sub(r'@(\w+)',
			r'<div style="position:inline-block"><form action="bitter.cgi" method="post" class="form-inline"><input type="hidden" name="username" value="\1"><button value="User_name" name="action" class="" style="border:0px">@\1</button></form></div>',result)
		result = re.sub(r'([^&])#(\w+)',
			r'\1<div style="position:inline-block"><form action="search_bleats.cgi" method="post" class="form-inline"><input type="hidden" name="key_word" value="#\2"><button value="search" name="action" class="" style="border:0px">#\2</button></form></div>',result)
		return result
	def print_reply(self):
		if self.in_reply_to == "":
			return ""
		else:
			import Search
			reply_to = Search.search_bleat_by_bleat_ID(self.in_reply_to)
			if reply_to.exist:
				return open(base+"reply_dropdown.html").read().format(reply_to.content + "<p/><strong> By:</strong>"+ reply_to.author)
			else:
				return ""
			return open(base+"reply_dropdown.html").read().format(self.in_reply_to)
	def format_bleat(self):
		return open(base+"single_bleat.html").read().format(self.print_loc_row(),
		self.print_reply(),self.format_content(),self.author,self.time,self.bleat_No)
	def __str__(self):
		#these returns need formating
		if self.exist:
			return self.content.__str__() + "Time" + self.time.__str__()
		else:
			return bleat_error


class User(Location,Picture):
	def __init__(self,UID = "null", username = default_str, full_name = default_str, 
	email = default_str, listens = default_str, password = default_str, longitude = default_str, 
	latitude = default_str, suburb = default_str,pic_dir = default_str,bleats = default_str,status=default_str,is_exist=True):
		if is_exist:
			self.UID = UID
			self.username = username
			self.full_name = full_name
			self.email = email
			self.listens = [var for var in re.split(r' ',listens) if var]
			self.password = password
			Location.__init__(self,longitude,latitude,suburb)
			if pic_dir == "":
				pic_dir="img/default.jpg"
			Picture.__init__(self,pic_dir)
			self.exist = is_exist
			self.status = status
			self.bleats = [var for var in re.split(r',',bleats) if var]
		else:
			self.exist = is_exist
	def __str__(self):
		string =""
		for key in self.attributes:
			string += key +":" + str(self.key)
	def print_bleats(self):
		l = list()
		if self.exist:
			l = [ Bleat(self.dataset_size,num) for num in self.bleats]
		return l
	def get_bleat_count(self):
		return len(self.bleats)
	def bleat_list(self):
		return self.bleats
	def add_bleats(self,bleat_No):
		if not bleat_No in self.bleats:
			self.bleats.append(bleat_No)
	def add_listens(self,username):
		if not username in self.listens:
			self.listens.append(username)
	def update(self):
		conn=sqlite3.connect("database/User.db")
		c = conn.cursor()
		bleats = ",".join(self.bleats)
		listens = " ".join(self.listens)
		operation = "INSERT OR REPLACE INTO users VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
		values=(self.UID, self.username, self.full_name, self.email,listens, self.password,
			self.longitude,self.latitude,self.suburb,self.pic_path,bleats,self.status)
		c.execute(operation,values)
		conn.commit()
		conn.close()
	def user_info(self):
		if self.exist:
			return open(base+"info_panel.html").read().format(img(self.pic_path).__str__(),self.username,self.print_loc(),self.full_name)
		else:
			return open(base+"info_panel.html").read().format(img("img/default.jpg").__str__(),"Unknown","Unknown","Unknown")
	def main_page(self):
		import Search
		#add to the user the bleats he follows
		for listening in self.listens:
			following = Search.search_user_by_ID_e(listening)
			for bleats in following.bleats:
				self.add_bleats(bleats)
		#add to the user the bleats mentioning him
		bleat_list = Search.search_bleat_by_content("@"+self.username)
		for bleat in bleat_list:
			self.add_bleats(bleat)
	def print_listening(self):
		string=""
		for listen in self.listens:
			string +=open(base+"listening_seg.html").read().format(listen)
		return open(base+"listening_panel.html").read().format(string)
	
	def print_bleats(self):
		import Search
		string=""
		def getKey(custom):
			return custom.time
		bleat_list=list()
		for bleat in self.bleats:
			try:
				bleat_list.append(Search.search_bleat_by_bleat_ID(bleat))
			except:
				continue
		for bleat in sorted(bleat_list,key=getKey,reverse=True):
			string += bleat.format_bleat()
		return open(base+"bleat_panel.html").read().format(string)
	def user_display(self):
		txt = open(base + "user_display.html").read()
		self.print_bleats()
		try:
			return txt.format(self.user_info(),
				self.print_listening(),self.print_bleats())+open(base + "style_bleat.html").read()
		except:
			#temporary for user not found
			return ""

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

def login_page_display(empty=False,not_exist=False,wrong=False):
	em="hidden"
	ex="hidden"
	wr="hidden"
	if empty:
		em=""
	elif not_exist:
		ex=""
	elif wrong:
		wr=""
	string = open(base + "login.html",'r').read().format("img/You-Shall-Not-Pass.png",
				em,ex,wr)
	return string + open(base+"style.html",'r').read()

def nav_bar_display(username):
	string = open(base+"navbar.html",'r').read()
	return string.format(my_account_menu(username,0))

def my_account_menu(username,password):
	return '''<li><a href="#">Dashboard</a></li>
            <li><a href="Logout.cgi" action="Logout">Logout</a></li>'''
      
def register_page():
	string = open(base+"register.html").read()
	return string