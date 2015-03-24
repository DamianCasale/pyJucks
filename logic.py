import zerorpc

class my_logic(object):
	def index(self):
		return zerorpc.Client("tcp://127.0.0.1:11111").index()

	def page1(self):
		return zerorpc.Client("tcp://127.0.0.1:11111").page1()

zServer = zerorpc.Server(my_logic())
zServer.bind("tcp://0.0.0.0:11110")
zServer.run()