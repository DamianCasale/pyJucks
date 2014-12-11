import json

from flask import render_template, request, Response
from app import app

@app.route('/')
def index():


	pageInfo = {
				'layout':	'layout_default.html',
				'template': 'page_index.html',
				'replaces': '#theMainContent',
				'data' : {
					'title':		'Playing with Jinja & Nunjucks',
					'renderedBy':	'Flask and Jinja2',
					'anEvent':		'Normal backend functionality',
					'aCounter':		0}}

	if request.is_xhr:
		pageInfo['data']['renderedBy']	= 'Nunjucks';
		pageInfo['data']['anEvent'] 	= 'Replaced in browser';
		return Response( json.dumps(pageInfo), mimetype='text/json')

	else:
		return render_template( pageInfo['template'], 
								layout		= pageInfo['layout'],
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'])

@app.route('/page1')
def page1():


	pageInfo = {
			'layout':	'layout_default.html',
			'template':	'page_page1.html',
		    'replaces':	'#theMainContent',
		    'data': {
					'title':		'Playing with Jinja & Nunjucks',
					'renderedBy':	'Flask and Jinja2',
					'anEvent':		'Normal backend functionality',
					'aCounter':		0}}


	if request.is_xhr:
		pageInfo['data']['renderedBy']	= 'Nunjucks';
		pageInfo['data']['anEvent'] 	= 'Replaced in browser';
		return Response( json.dumps(pageInfo), mimetype='text/json')

	else: 
		return render_template( pageInfo['template'],
								layout		= pageInfo['layout'],
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'])