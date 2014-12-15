var nunEnv		= nunjucks.configure('static/templates');


$(document).on('click', '.ajaxableLink', function(e){
	e.preventDefault();

	$.get(this.href, function( data ){

		/* set the layout to the non layout 
		*  so we dont pull in a whole page 
		*  into a part of the page
		*/
		data.data.layout = "layout_none.html";

		/* Replace main template */
		$(data.replaces).html( nunEnv.render( data.template, data.data) );

		/* if there are partials */
		if( data.partials ) {
			/* replace them */
			for ( i=0;i<data.partials.length;i++) {
				$(data.partials[i].replaces).html( nunEnv.render( data.partials[i].template, data.partials[i].data ));
			}
		}
	});
});