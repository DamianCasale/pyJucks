pyJucks
=======

Playing with Python, Flask, Jinja2 and Nunjucks 

http://mozilla.github.io/nunjucks/


Requirements
============

python

flask (pip install flask)

node.js is required for the precompilation of nunjucks templates

npm is required for pulling down nunjucks

nunjucks node module (npm install nunjucks) includes nunjucks-slim.js and the precompiler


------------


Before first run and after alteration, the templates must be compiled for use by nunjucks-slim on the front end using :

    node nunjucks-compile app/templates/ > app/static/js/templates.js


------------


ToDo :

check and sort backwards browser compatibility
