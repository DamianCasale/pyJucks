import zerorpc

from app.data.models.user import User

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

    def getUserData(self,username):
        return User.getUserData(username)

zServer = zerorpc.Server(my_data())
zServer.bind("tcp://0.0.0.0:11111")
zServer.run()