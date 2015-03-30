import zerorpc

from app.data.models.user import User
from app.data.models.space import Space

class my_data(object):

    def index(self):
        return {
            'title':		'Index : Playing with Jinja & Nunjucks',
            'renderedBy':	'Flask and Jinja2 via ZeroMQ',
            'anEvent':		'Normal backend From DATA',
            'aCounter':		0
        }

    def page1(self):

        userlist = []
        for user in User.objects:
            userlist.append(user.email)

        return {
            'title':		'Page1 : Playing with Jinja & Nunjucks',
            'renderedBy':  'Flask and Jinja2 via ZeroMQ',
            'anEvent':		userlist,
            'aCounter':		0
        }

    def isValidUsername(self,username):
        return User.isValidUsername(username)

    def getUserData(self,userId):
        return User.getUserData(userId)

    def getUserSpaces(self,userId):
        return Space.getUserSpaces(userId)

    def getUserLogin(self,username,password):
        return User.getUserLogin(username,password)

zServer = zerorpc.Server(my_data())
zServer.bind("tcp://0.0.0.0:11111")
zServer.run()