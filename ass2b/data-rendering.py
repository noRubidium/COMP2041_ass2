#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re,os,glob,sqlite3
import shutil
import special_char_filter
conn = sqlite3.connect('database/User.db')
c = conn.cursor()
default_str = ""
try:
	c.execute('''CREATE TABLE users
		(userID INTEGER PRIMARY KEY, username TEXT,
			full_name TEXT, email TEXT,listens TEXT,
			password TEXT, home_longitude REAL, home_latitude REAL, 
			home_suburb REAL, picture_dir TEXT,bleats TEXT,status TEXT);''')

	print glob.glob("dataset-large/users/*")
	UID = 0
	for user_dir in glob.glob("dataset-large/users/*"):
		details_filename = os.path.join(user_dir, "details.txt")
		bleats_filename = os.path.join(user_dir,"bleats.txt")
		txt = re.split(r'\n',open(details_filename,'r').read())
		print txt
		full_name = default_str
		home_longitude = default_str
		home_latitude = default_str
		home_suburb = default_str
		listens = default_str
		username = default_str
		email= default_str
		password = default_str
		status = default_str
		if os.path.isfile(user_dir+"/profile.jpg"):
			picture_dir ='user_img/'+str(UID)+"_profile.jpg"
			shutil.copy2(user_dir+"/profile.jpg", picture_dir)
		else:
			picture_dir = default_str
		for line in txt:
			print line
			if re.match(r'^\s*username:',line):
				username = re.sub(r'^\s*username:\s*','',line)
				print username
			elif re.match(r'^\s*password:',line):
				password = re.sub(r'^\s*password:\s*','',line)
			elif re.match(r'^\s*full_name:',line):
				full_name = re.sub(r'^\s*full_name:\s*','',line)
			elif re.match(r'^\s*email:',line):
				email = re.sub(r'^\s*email:\s*','',line)
			elif re.match(r'^\s*listens:',line):
				listens = re.sub(r'^\s*listens:\s*','',line)
			elif re.match(r'^\s*home_longitude:',line):
				home_longitude = re.sub(r'^\s*home_longitude:\s*','',line)
			elif re.match(r'^\s*home_latitude:',line):
				home_latitude = re.sub(r'^\s*home_latitude:\s*','',line)
			elif re.match(r'^\s*home_suburb:',line):
				home_suburb = re.sub(r'^\s*home_suburb:\s*','',line)
		txt = open(bleats_filename,'r').read()
		txt = re.sub(r'\n',',',txt)
		sets = (UID,username,full_name,email,listens,password,home_longitude,home_latitude,home_suburb,picture_dir,txt,status)
		operation = '''INSERT INTO users values(?,?,?,?,?,?,?,?,?,?,?,?);'''
		c.execute(operation,sets)
		UID += 1
	conn.commit()
	conn.close()
except:
	conn.close()
	
conn = sqlite3.connect('database/Bleats.db')
c = conn.cursor()

try:
	c.execute('''CREATE TABLE bleats
		(bleatID INTEGER PRIMARY KEY, username TEXT,
			bleat TEXT,in_reply_to TEXT,time TEXT,
			 longitude REAL, latitude REAL,mentioned_by TEXT);''')
except:
	pass
for bleat_dir in glob.glob("dataset-large/bleats/*"):
	bleat_No = re.sub(r'dataset-large/bleats/','',bleat_dir)
	time=default_str
	username = default_str
	in_reply_to = ""			
	longitude = default_str
	latitude = default_str
	txt = re.split(r'\n',open(bleat_dir,'r').read())
	for line in txt:
		if re.match(r'^\s*bleat:',line):
			content = re.sub(r'^\s*bleat:\s*','',line)
			content = special_char_filter.special_char_filter(content)
		elif re.match(r'^\s*time:',line):
			time = re.sub(r'^\s*time:\s*','',line)
		elif re.match(r'^\s*username:\s*',line):
			username =  re.sub(r'^\s*username:\s*','',line)
		elif re.match(r'^\s*longitude:\s*',line):
			longitude =  re.sub(r'^\s*longitude:\s*','',line)
		elif re.match(r'^\s*latitude:\s*',line):
			latitude =  re.sub(r'^\s*latitude:\s*','',line)
		elif re.match(r'^\s*in_reply_to:',line):
			in_reply_to =  re.sub(r'^\s*in_reply_to:\s*','',line)
	settings = (bleat_No,username,content,in_reply_to,time,longitude,latitude,"")
	operation = '''INSERT INTO bleats values(?,?,?,?,?,?,?,?)'''
	c.execute(operation,settings)
conn.commit()
conn.close()
