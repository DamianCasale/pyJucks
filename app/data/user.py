import zerorpc
import json

class loginUserObject():

	def __init__(self,username):
		self.data = dict(json.loads(getUserData(username)))

	def is_authenticated(self):
		return self.is_authenticated

	def get_id(self):
		return self.data['email']

	def is_active(self):
		return self.data['is_active']

def getLoginUserObject(username):
	return loginUserObject(username)

def isValidUsername(username):
	return zerorpc.Client("tcp://127.0.0.1:11110").isValidUsername(username)

def getUserData(username):
	return zerorpc.Client("tcp://127.0.0.1:11110").getUserData(username)