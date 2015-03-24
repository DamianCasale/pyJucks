import zerorpc

from app.logic.site import getIndex, getPage1

class my_logic(object):
	def index(self):
		return getIndex()

	def page1(self):
		return getPage1()

zServer = zerorpc.Server(my_logic())
zServer.bind("tcp://0.0.0.0:11110")
zServer.run()