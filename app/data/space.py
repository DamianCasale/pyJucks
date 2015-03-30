import zerorpc

def getUserSpaces(userId):
		return zerorpc.Client("tcp://127.0.0.1:11110").getUserSpaces(userId)
