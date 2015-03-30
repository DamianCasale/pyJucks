import json

from flask import render_template, request, Response, session
from app import app
from app.data.site import getIndex
from flask.ext.login import current_user
@app.route('/')
def index():
	
	try:
		data = getIndex()

	except Exception, e:
		return "Error Getting Index Page Data : %s"%e,500

	pageInfo = {
				'layout':	'layout_default.html',
				'template': 'page_index.html',
				'replaces': '#theMainContent',
				'data': data,
				'user': current_user.to_json(),
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
		pageInfo['data']['renderedBy']				 	= 'Nunjucks';
		pageInfo['data']['anEvent'] 				 	= 'Replaced in browser';
		pageInfo['partials'][0]['data']['notification'] = 'index from front';

		return Response( json.dumps(pageInfo), mimetype='text/json')

	else:
		return render_template( pageInfo['template'], 
								layout		= pageInfo['layout'],
								user		= current_user,
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'],
								notification = pageInfo['partials'][0]['data']['notification'])