var theCounter	= 1;

var theButton	= document.getElementById('theButton');
var toReplace	= document.getElementById('toReplace');

var nunEnv		= nunjucks.configure('static/templates');

theButton.addEventListener('click', function() {
	var rendered		= nunEnv.render('partial/first.html', { 'aVariable':' Here I am', 'aCounter':theCounter });
	toReplace.innerHTML	= rendered;
	theCounter++;
});