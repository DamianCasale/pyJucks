from flask import render_template, request
from app import app

@app.route('/')
def index():
	return render_template("index.html",
                           title='Playing with Jinja & Nunjucks',
                           renderedBy='Flask and Jinja2',
                           anEvent='Normal backend functionality',
                           aCounter=0)

@app.route('/page1')
def page1():

	if request.is_xhr: 
		print "XHR REQUEST"
		#here we should send back only the json describing the page to be rendered via Nunjucks
	else: 
		print "NON XHR"
		#here should be the normal page render
		return render_template("page1.html",
		                   title='Playing with Jinja & Nunjucks',
                           renderedBy='Flask and Jinja2',
                           anEvent='Normal backend functionality',
                           aCounter=0)