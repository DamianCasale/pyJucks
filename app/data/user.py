import zerorpc
import json

from app import login_manager

@login_manager.user_loader
def load_user(userId):
	return getLoginUserObject(userId)

class loginUserObject():

	def __init__(self,id):

		tempUserData = json.loads(getUserData(id))

		self.id = tempUserData['_id']['$oid']
		self._id = self.id
		self.active = tempUserData['is_active']
		self.email = tempUserData['email']

	def to_json(self):
		return json.dumps({
			"email": self.email,
			"active": self.active
		})

	def get_id(self):
		return self.id

	def get_email(self):
		return self.email

	def is_authenticated(self):
		return self.is_authenticated

	def is_anonymous(self):
		return self.is_anonymous

	def is_active(self):
		return self.is_active

def getLoginUserObject(userId):
	return loginUserObject(userId)

def isValidUsername(username):
	return zerorpc.Client("tcp://127.0.0.1:11110").isValidUsername(username)

def getUserData(userId):
	return zerorpc.Client("tcp://127.0.0.1:11110").getUserData(userId)

def getUserLogin(username,password):
	ret = json.loads(zerorpc.Client("tcp://127.0.0.1:11110").getUserLogin(username,password))
	return loginUserObject(ret['_id']['$oid'])