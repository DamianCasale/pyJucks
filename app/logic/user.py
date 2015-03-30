import zerorpc

def isValidUsername(username):
	return zerorpc.Client("tcp://127.0.0.1:11111").isValidUsername(username)

def getUserData(userId):
	return zerorpc.Client("tcp://127.0.0.1:11111").getUserData(userId)

def getUserLogin(username,password):
	return zerorpc.Client("tcp://127.0.0.1:11111").getUserLogin(username,password)