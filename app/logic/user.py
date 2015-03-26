import zerorpc

def isValidUsername(username):
	return zerorpc.Client("tcp://127.0.0.1:11111").isValidUsername(username)

def getUserData(username):
	return zerorpc.Client("tcp://127.0.0.1:11111").getUserData(username)