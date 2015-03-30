import json

from flask import render_template, request, Response, session
from app import app
from app.data.space import getUserSpaces

from flask.ext.login import login_required, current_user

@app.route('/space')
@login_required
def space():

	try:
		spaces = json.loads(getUserSpaces(current_user.get_id()))
		print "SPACES %s"% spaces
	except Exception, e:
		return "Error Getting space Data : %s"%e,500

	pageInfo = {
				'layout':	'layout_default.html',
				'template':	'page_space.html',
		    	'replaces':	'#theMainContent',
		    	'spaces': spaces,
				'user': current_user.to_json(),
				'partials':[
					{
						'template': 'partial_navbar.html',
						'replaces': '#theNavbar',
						'data' : {
							'notification':'space from back'
						}
					}
				]}

	if request.is_xhr:
		pageInfo['data'] = {}
		pageInfo['data']['renderedBy']					= 'Nunjucks';
		pageInfo['data']['anEvent']						= 'Replaced in browser';
		pageInfo['partials'][0]['data']['notification'] = 'space from front';

		return Response( json.dumps(pageInfo), mimetype='text/json')

	else: 
		return render_template( pageInfo['template'],
								layout		= pageInfo['layout'],
								user		= current_user,
								spaces		= spaces,
								notification = pageInfo['partials'][0]['data']['notification'])