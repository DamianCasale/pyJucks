import json

from flask import render_template, request, Response
from app import app, celery
from app.logic import my_logic

@app.route('/')
def index():

	data = my_logic.delay()

	pageInfo = {
				'layout':	'layout_default.html',
				'template': 'page_index.html',
				'replaces': '#theMainContent',
				'data' : data.get(),
				'partials':[
					{
						'template': 'partial_navbar.html',
						'replaces': '#theNavbar',
						'data' : {
							'notification':'index from back'
						}
					}
				]}

	if request.is_xhr:
		pageInfo['data']['renderedBy']				 = 'Nunjucks';
		pageInfo['data']['anEvent'] 				 = 'Replaced in browser';
		pageInfo['partials'][0]['data']['notification'] = 'index from front';

		return Response( json.dumps(pageInfo), mimetype='text/json')

	else:
		return render_template( pageInfo['template'], 
								layout		= pageInfo['layout'],
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'],
								notification = pageInfo['partials'][0]['data']['notification'])