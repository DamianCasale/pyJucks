import time
from app import PyRpc

def my_data():
    print "I am data"
    return {
					'title':		'Page1 : Playing with Jinja & Nunjucks',
					'renderedBy':	'Flask and Jinja2',
					'anEvent':		'Normal backend functionality',
					'aCounter':		0
				}

myRpc = PyRpc("com.myCompany.MyApplication2")


myRpc.publishService(my_data)
myRpc.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    myRpc.stop()