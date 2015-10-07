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
	def __init__(self,longitude=default_str,latitude=default_str,suburb=default_str):
		self.longitude = longitude
		self.latitude = latitude
		self.suburb = suburb
	def __str__(self):
		return self.print_loc_row()
	def print_loc_row(self):
		return '''<span class="glyphicon glyphicon-map-marker location-mark menu-mark">
		<div class="panel">
			<ul class="list-unstyled">
				<li><strong>Longitude:</strong> {0}</li>
				<li><strong>Latitude:</strong> {1}</li>
			</ul>
		</div>
		</span>'''.format(self.longitude,self.latitude)
	def get_long(self):
		return '''<div class="row">
			<div class="col-xs-4"><strong>longitude</strong></div>
			<div class="col-xs-8">{0}</div>
			</div>'''.format(self.longitude)
	def get_lat(self):
		return '''<div class="row">
			<div class="col-xs-4"><strong>Latitude</strong></div>
			<div class="col-xs-8">{0}</div>
			</div>'''.format(self.latitude)
	def get_sub(self):
		return '''<div class="row">
			<div class="col-xs-4"><strong>Suburb</strong></div>
			<div class="col-xs-8">{0}</div>
			</div>'''.format(self.suburb)
	def print_loc(self):
		return self.get_long()+self.get_lat() +self.get_sub()

# UserDetail includes the detailed information of the user
# taking in the file directory including the user's info
class UserDetail(Location):
	def __init__(self,user_dir):
		full_name = "<b>"+default_str+"</b>"
		longitude = default_str
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
				elif re.match(r'^\s*home_longitude:',line):
					longitude = re.sub(r'^\s*home_longitude:\s*','',line)
				elif re.match(r'^\s*home_latitude:',line):
					latitude = re.sub(r'^\s*home_latitude:\s*','',line)
				elif re.match(r'^\s*home_suburb:',line):
					suburb = re.sub(r'^\s*home_suburb:\s*','',line)
			Location.__init__(self,longitude,latitude,suburb)
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
	def user_name(self):
		return self.username
	def full_name(self):
		return self.full_name

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
			longitude = default_str
			latitude = default_str
			for line in txt:
				if re.match(r'^\s*bleat:',line):
					content = re.sub(r'^\s*bleat:\s*','',line)
				elif re.match(r'^\s*time:',line):
					time = re.sub(r'^\s*time:\s*','',line)
					time = datetime.datetime(1970,1,1) + datetime.timedelta(0,int(time))
				elif re.match(r'^\s*username:\s*',line):
					username =  re.sub(r'^\s*username:','',line)
				elif re.match(r'^\s*longitude:\s*',line):
					longitude =  re.sub(r'^\s*longitude:','',line)
				elif re.match(r'^\s*latitude:\s*',line):
					latitude =  re.sub(r'^\s*latitude:','',line)
				elif re.match(r'^\s*in_reply_to:',line):
					in_reply_to =  re.sub(r'^\s*in_reply_to:\s*','',line)
			Location.__init__(self,longitude,latitude)
			self.content = content
			self.time = time
			self.author = username
			self.in_reply_to = in_reply_to
			self.exist = True
		else:
			self.exist = False
	def print_reply(self):
		if self.in_reply_to == "":
			return ""
		else:
			return '''<span class="glyphicon glyphicon-new-window menu-mark in_reply_to-mark">
						<div class="text-left">
							<ul class="list-unstyled">
								<li><strong>In reply to:</strong> {0}</li>
							</ul>
						</div>
					</span>'''.format(self.in_reply_to)
	def format_bleat(self):
		return '''
		<div class="list-group">
			<div class="list-group-item container">
				<div class="col-sm-12">{2}</div>
				<div class="col-sm-1">{0}</div>
				<div class="col-sm-1" align="right">
					{1}
				</div>
				<div class="col-sm-4">{3}</div>
				<div class="col-sm-6" align="right"><h6><small>{4}</small></h6></div>

			</div>
		</div>
		<div class="list-group">
		</div>
		'''.format(self.print_loc_row(),self.print_reply(),self.content,self.author,self.time)
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
	def bleat_list(self):
		return self.bleats
