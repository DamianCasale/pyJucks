var theCounter	= 1;

var theButton	= document.getElementById('theButton');
var toReplace	= document.getElementById('toReplace');

var nunEnv		= nunjucks.configure('static/partials');


theButton.addEventListener('click', function() {
	var rendered		= nunEnv.render('first.html', { 'renderedBy':'Nunjucks',
														'anEvent':' Replaced in browser', 
														'aCounter':theCounter });
	toReplace.innerHTML	= rendered;
	theCounter++;
});







$('.ajaxableLink').on('click', function(e){
	e.preventDefault();
	alert("Ajaxable link clicked : " + this.href);

	$.get(this.href, function( data ){
		alert( "The ajax request returned : " + data );
	});

});