from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template("index.html",
                           title='Playing with Jinja & Nunjucks',
                           user={ 'name':'Damian'},
                           renderedBy='Flask and Jinja2',
                           anEvent='Normal backend functionality',
                           aCounter=0)