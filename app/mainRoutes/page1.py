import json

from flask import render_template, request, Response
from app import app, RpcConnection

remote = RpcConnection("com.myCompany.MyLogic")

@app.route('/page1')
def page1():

	data = remote.call("my_logic").result

	print "DINGO :: %s" % data
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

remote.close()