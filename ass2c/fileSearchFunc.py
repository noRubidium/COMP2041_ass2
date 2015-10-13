#!/usr/bin/python

import glob, re, os

# Pre-con use a username or a user's name to find the matching user(s)
# Post-con return a list of matching users
def find_user(dataset_size,username):
	filelist =list()
	#if the username input is empty, we will only return nothing.
	if username == "":
		return filelist
	users_dir = "dataset-"+dataset_size+"/users"
	user_list = glob.glob(users_dir+"/*")
	for dirname in user_list:
		if re.sub(users_dir+"/",'',dirname) == username:
			filelist.append(dirname)
	for dirname in user_list:
		f = open(dirname+"/details.txt",'r')
		txt = f.read()
		line = re.findall(r'full_name:\s*[^\n]+\s*\n',txt,re.I)
		name = re.sub(r'full_name:\s*([^\n]+)\s*\n',r'\1',line[0])
		if re.match(username,name,re.I):
			filelist.append(dirname)
	return filelist
def find_user_byID(dataset_size,username):
	user_dir = "dataset-"+dataset_size+"/users/"+username
	if os.path.isdir(user_dir):
		return user_dir
	else:
		return ""