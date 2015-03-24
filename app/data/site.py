import zerorpc

def getIndex():
		return zerorpc.Client("tcp://127.0.0.1:11110").index()

def getPage1():
		return zerorpc.Client("tcp://127.0.0.1:11110").page1()