import json

from flask import render_template, request
from app import app

@app.route('/')
def index():


	pageInfo = {
				'template': 'index.html',
				'replaces': 'theMainContent',
				'data' : {
					'title':		'Playing with Jinja & Nunjucks',
					'renderedBy':	'Flask and Jinja2',
					'anEvent':		'Normal backend functionality',
					'aCounter':		0}}

	if request.is_xhr:
		return json.dumps(pageInfo)

	else:
		return render_template( pageInfo['template'], 
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'])

@app.route('/page1')
def page1():


	pageInfo = {
			'template':	'page1.html',
		    'replaces':	'theMainContent',
		    'data': {
					'title':		'Playing with Jinja & Nunjucks',
					'renderedBy':	'Flask and Jinja2',
					'anEvent':		'Normal backend functionality',
					'aCounter':		0}}


	if request.is_xhr: 
		print "XHR REQUEST"
		#here we should send back only the json describing the page to be rendered via Nunjucks
		return json.dumps(pageInfo)
	else: 
		print "NON XHR"
		#here should be the normal page render
		return render_template( pageInfo['template'], 
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'])