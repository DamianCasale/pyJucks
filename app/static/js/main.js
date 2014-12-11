var theCounter	= 1;
var nunEnv		= nunjucks.configure('static/templates');

var attatchEvents = function () {
	
	if ($('#theButton')) {
		$('#theButton').on('click', function() {
			$('#toReplace').html( nunEnv.render('partial_first.html', { 'renderedBy':'Nunjucks',
																'anEvent':' Replaced in browser', 
																'aCounter':theCounter }));
			theCounter++;
		});
	}
}

attatchEvents();


$('.ajaxableLink').on('click', function(e){
	e.preventDefault();

	$.get(this.href, function( data ){

		/* set the layout to the non layout 
		*  so we dont pull in a whole page 
		*  into a part of the page
		*/
		data.data.layout = "layout_none.html";

		$(data.replaces).html( nunEnv.render( data.template, data.data) );
		attatchEvents();
	});

});