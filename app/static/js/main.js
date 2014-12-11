var theCounter	= 1;

var theButton	= document.getElementById('theButton');
var toReplace	= document.getElementById('toReplace');

var nunEnv		= nunjucks.configure('static/partials');

theButton.addEventListener('click', function() {
	var rendered		= nunEnv.render('first.html', { 'renderedBy':'Nunjucks in browser!',
														'anEvent':' Replaced on in browser', 
														'aCounter':theCounter });
	toReplace.innerHTML	= rendered;
	theCounter++;
});