import sqlite3
import Html
#global
default_str = ""
base ="../database/"
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
		operation += "ORDERED BY "+order_by+" DESC"
	c.execute(operation.format(table,field,value))
	w=c.fetchall()
	return w	

def search_bleat_by_bleat_ID(value):
	db_filename = base+"Bleats.db"
	table = "bleats"
	field = "bleatID"
	l=search(db_filename,table,field,value)
	if len(l) > 0:
		w = l[0]
		bleat = Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6])
	else:
		bleat = Html.Bleat(is_exist = False)
	return bleat

def search_bleat_by_username(value):
	db_filename = base+"Bleats.db"
	table = "bleats"
	field = "username"
	bleats = list()
	for w in search(db_filename,table,field,value,order_by = "time"):
		bleats.append(Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6]))
	return bleats

def search_bleat_by_content(value):
	db_filename = base+"Bleats.db"
	table = "bleats"
	field = "bleat"
	value = "%" + value + "%"
	bleats = list()
	for w in search(db_filename,table,field,value,True,order_by = "time"):
		bleats.append(Html.Bleat(w[0],w[1],w[2],w[3],w[4],w[5],w[6]))
	return bleats
#search by userID exact
def search_user_by_ID_e(value):
	db_filename = base+"User.db"
	table = "users"
	field = "username"
	l = search(db_filename,table,field,value)
	if len(l) > 0:
		w=l[0]
		user = Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10])
	else:
		user = Html.User(is_exist = False)
	return user
	
#search by arbitrary user ID arbitrary
def search_user_by_full_name(value):
	db_filename = base+"User.db"
	table = "users"
	field = "username"
	users = list()
	value = "%" + value + "%"
	for w in search(db_filename,table,field,value,True):
		users.append( Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10]))
	return users
	
#search by arbitrary user ID
def search_user_by_full_name(value):
	db_filename = base+"User.db"
	table = "users"
	field = "full_name"
	users = list()
	value = "%" + value + "%"
	for w in search(db_filename,table,field,value,True):
		users.append( Html.User(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10]))
	return users
