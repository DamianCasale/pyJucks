import json

from flask import render_template, request, Response
from app import app
from app.data.site import getPage1

@app.route('/page1')
def page1():

	try:
		data = getPage1()

	except Exception, e:
		return "Error Getting Page 1 Data : %s"%e,500

	pageInfo = {
				'layout':	'layout_default.html',
				'template':	'page_page1.html',
		    	'replaces':	'#theMainContent',
		    	'data': data,
				'partials':[
					{
						'template': 'partial_navbar.html',
						'replaces': '#theNavbar',
						'data' : {
							'notification':'page 1 from back'
						}
					}
				]}

	if request.is_xhr:
		pageInfo['data']['renderedBy']					= 'Nunjucks';
		pageInfo['data']['anEvent']						= 'Replaced in browser';
		pageInfo['partials'][0]['data']['notification'] = 'page 1 from front';

		return Response( json.dumps(pageInfo), mimetype='text/json')

	else: 
		return render_template( pageInfo['template'],
								layout		= pageInfo['layout'],
								title		= pageInfo['data']['title'],
								renderedBy	= pageInfo['data']['renderedBy'],
								anEvent		= pageInfo['data']['anEvent'],
								aCounter	= pageInfo['data']['aCounter'],
								notification = pageInfo['partials'][0]['data']['notification'])