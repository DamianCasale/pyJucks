import zerorpc

class my_data(object):

    def index(self):
        return {
            'title':		'Index : Playing with Jinja & Nunjucks',
            'renderedBy':	'Flask and Jinja2 via ZeroMQ',
            'anEvent':		'Normal backend From DATA',
            'aCounter':		0
        }

    def page1(self):
        return {
            'title':		'Page1 : Playing with Jinja & Nunjucks',
            'renderedBy':	'Flask and Jinja2 via ZeroMQ',
            'anEvent':		'Normal backend From DATA',
            'aCounter':		0
        }

zServer = zerorpc.Server(my_data())
zServer.bind("tcp://0.0.0.0:11111")
zServer.run()