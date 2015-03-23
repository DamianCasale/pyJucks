from app import celery

@celery.task
def my_data():
    # return data
    print "I am data"
    return {
				'title':		'Index : Playing with Jinja & Nunjucks',
				'renderedBy':	'Flask and Jinja2',
				'anEvent':		'Normal backend functionality',
				'aCounter':		0
			}