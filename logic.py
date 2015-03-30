import zerorpc

from app.logic import site
from app.logic import user
from app.logic import space

class my_logic(object):
	def index(self):
		return site.getIndex()

	def page1(self):
		return site.getPage1()

	def isValidUsername(self, username):
		return user.isValidUsername(username)

	def getUserData(self, userId):
		return user.getUserData(userId)

	def getUserSpaces(self, userId):
		return space.getUserSpaces(userId)

	def getUserLogin(self, username,password):
		return user.getUserLogin(username,password)

zServer = zerorpc.Server(my_logic())
zServer.bind("tcp://0.0.0.0:11110")
zServer.run()