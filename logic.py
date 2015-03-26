import zerorpc

from app.logic import site
from app.logic import user

class my_logic(object):
	def index(self):
		return site.getIndex()

	def page1(self):
		return site.getPage1()

	def isValidUsername(self, username):
		return user.isValidUsername(username)

	def getUserData(self, username):
		print "logic : %s"%user.getUserData(username)
		return user.getUserData(username)

zServer = zerorpc.Server(my_logic())
zServer.bind("tcp://0.0.0.0:11110")
zServer.run()