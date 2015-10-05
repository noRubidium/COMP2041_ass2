import glob, re
import os.path
import datetime


###############################################
## Classes library written by Minjie Shen    ##
## including basic classes that can be used  ##
## to make the bitter life easier. should be ##
## used with the Html library written by me  ##
## for some of the supporting function.      ##
###############################################

# This section define some global variables
default_str = "Unknown"
bleat_error = "This bleat unavailable (has been deleted or not wrong reference)."
user_not_exist = "This user does not exist in the data base!"


# definition of all types of classes

# location can be used to store location and calculate the distance and many things
# it's one of the super classes
class Location(object):
	def __init__(self,longtitude=default_str,latitude=default_str,suburb=default_str):
		self.longtitude = longtitude
		self.latitude = latitude
		self.suburb = suburb
	def __str__(self):
		return "<div>\n<div>Longtitude</div><div></div>"

# UserDetail includes the detailed information of the user
# taking in the file directory including the user's info
class UserDetail(Location):
	def __init__(self,user_dir):
		full_name = "<b>"+default_str+"</b>"
		longtitude = default_str
		latitude = default_str
		suburb = default_str
		listens = list()
		user_loc = user_dir + "/details.txt"
		if os.path.isfile(user_loc):
			txt = re.split(r'\n',open(user_loc,'r').read())
			for line in txt:
				if re.match(r'^\s*username:',line):
					username = re.sub(r'^\s*username:\s*','',line)
				elif re.match(r'^\s*password:',line):
					password = re.sub(r'^\s*password:\s*','',line)
				elif re.match(r'^\s*full_name:',line):
					full_name = re.sub(r'^\s*full_name:\s*','',line)
				elif re.match(r'^\s*email:',line):
					email = re.sub(r'^\s*email:\s*','',line)
				elif re.match(r'^\s*listens:',line):
					listen_string = re.sub(r'^\s*listens:\s*','',line)
					listens = re.split(r'\s',listen_string)
			Location.__init__(self,longtitude,latitude,suburb)
			self.username = username
			self.password = password
			self.full_name = full_name
			self.email = email
			self.listens = listens
			self.exist = True
		else :
			self.exist = False
	def __str__(self):
		if self.exist:
			pass
		else:
			return user_not_exist

# Picture class can be used to store the user's photo location 
# and may print the photo in a nicely formated 
class Picture(object):
	def __init__(self,picdir):
		self.pic_path = picdir
	def __str__(self):
		return Html.img(self.pic_path).__str__()


# Bleat class can be used to store the bleats
class Bleat(Location):
	def __init__(self,dataset_size,bleats_num):
		bleats_dir = "dataset-" + dataset_size + "/bleats"
		bleat_loc = bleats_dir + "/"+bleats_num
		if os.path.isfile(bleat_loc):
			bleat_file = open(bleat_loc,'r')
			txt = re.split(r'\n',bleat_file.read())
			# Set default value to some variables
			in_reply_to = ""			
			longtitude = default_str
			latitude = default_str
			for line in txt:
				if re.match(r'^\s*bleat:',line):
					content = re.sub(r'^\s*bleat:\s*','',line)
				elif re.match(r'^\s*time:',line):
					time = re.sub(r'^\s*time:\s*','',line)
					time = datetime.datetime(1970,1,1) + datetime.timedelta(0,int(time))
				elif re.match(r'^\s*username:\s*',line):
					username =  re.sub(r'^\s*username:','',line)
				elif re.match(r'^\s*longtitude:\s*',line):
					longtitude =  re.sub(r'^\s*longtitude:','',line)
				elif re.match(r'^\s*latitude:\s*',line):
					latitude =  re.sub(r'^\s*latitude:','',line)
				elif re.match(r'^\s*in_reply_to:',line):
					in_reply_to =  re.sub(r'^\s*in_reply_to:\s*','',line)
			Location.__init__(self,longtitude,latitude)
			self.content = content
			self.time = time
			self.author = username
			self.exist = True
		else:
			self.exist = False
	def __str__(self):
		#these returns need formating
		if self.exist:
			return self.content.__str__() + "Time" + self.time.__str__()
		else:
			return bleat_error


class User(UserDetail,Picture):
	def __init__(self,dataset_size,userdir):
		UserDetail.__init__(self,userdir)
		if os.path.isfile(userdir+"/profile.jpg"):
			Picture.__init__(self,userdir+"/profile.jpg")
		else:
			Picture.__init__(self,"img/default.jpg")
		f = open(userdir+"/bleats.txt",'r')
		txt = f.read()
		# self.bleats = 
		self.bleats = [var for var in re.split(r'\n+',txt) if var]
		self.dataset_size = dataset_size
	def __str__(self):
		pass
	def print_bleats(self):
		l = list()
		l = [ Bleat(self.dataset_size,num) for num in self.bleats]
		for var in l:
			print var 
			print "<p/>"
		return l
	def get_bleat_count(self):
		return len(self.bleats)

