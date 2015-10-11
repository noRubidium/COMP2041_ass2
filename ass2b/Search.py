import sqlite3
import Html,re
#global
default_str = ""
#generic search function
def search(database,table,field,value,is_partial = False,order_by = default_str ):
	db_filename = database
	conn = sqlite3.connect(db_filename)
	c = conn.cursor()
	if not is_partial:
		operation="SELECT * FROM {0} WHERE {1} = '{2}'"
	else:
		operation="SELECT * FROM {0} WHERE {1} LIKE '{2}'"
	if not order_by == default_str:
		operation += "ORDERED BY "+order_by+" ASC"
	c.execute(operation.format(table,field,value))
	w=c.fetchall()
	
	return w	

def search_bleat_by_bleat_ID(value):
	db_filename = "database/Bleats.db"
	table = "bleats"
	field = "bleatID"
	l=search(db_filename,table,field,value)
	w=list()
	if len(l) > 0:
		u = l[0]
		for i in range(0,len(u)):
			w.append(re.sub(r'^"\s*','',str(u[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		bleat = Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6])
	else:
		bleat = Html.Bleat(is_exist = False)
	return bleat

def search_bleat_by_username(value):
	db_filename = "database/Bleats.db"
	table = "bleats"
	field = "username"
	bleats = list()
	
	for l in search(db_filename,table,field,value,order_by = "time"):
		w=list()
		for i in range(0,len(l)):
			w.append(re.sub(r'^"\s*','',str(l[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		bleats.append(Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6]))
	bleats.reverse()
	return bleats

def search_bleat_by_content(value):
	db_filename = "database/Bleats.db"
	table = "bleats"
	field = "bleat"
	value = "%" + value + "%"
	bleats = list()

	for l in search(db_filename,table,field,value,True,order_by = "time"):
		w=list()
		for i in range(0,len(l)):
			w.append(re.sub(r'^"\s*','',str(l[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		bleats.append(Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6]))
	return bleats
#search by userID exact
def search_user_by_ID_e(value):
	db_filename = "database/User.db"
	table = "users"
	field = "username"
	w=list()
	l = search(db_filename,table,field,value)
	if len(l) > 0:
		u=l[0]
		for i in range(0,len(u)):
			w.append(re.sub(r'^"\s*','',str(u[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		user = Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10])
	else:
		user = Html.User(is_exist = False)
	return user
	
#search by arbitrary user ID arbitrary
def search_user_by_ID_a(value):
	db_filename = "database/User.db"
	table = "users"
	field = "username"
	users = list()
	
	value = "%" + value + "%"
	for l in search(db_filename,table,field,value,True):
		w=list()
		for i in range(0,len(l)):
			w.append(re.sub(r'^"\s*','',str(l[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		users.append( Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10]))
	return users
	
#search by arbitrary user ID
def search_user_by_full_name(value):
	db_filename = "database/User.db"
	table = "users"
	field = "full_name"
	users = list()

	value = "%" + value + "%"
	for l in search(db_filename,table,field,value,True):
		w=list()
		for i in range(0,len(l)):
			w.append(re.sub(r'^"\s*','',str(l[i])))
			w[i] = re.sub(r'"\s*$','',w[i])
			w[i] = re.sub(r'\&prime\;',"'",w[i])
		users.append( Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10]))
	return users
