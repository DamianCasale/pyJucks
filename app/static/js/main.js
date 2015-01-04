var nunEnv		= nunjucks.configure('static/templates');

var	History = window.History,
	State = History.getState();

History.log('initial:', State.data, State.title, State.url);

/*
Bind to State Change
*/
History.Adapter.bind(window,'statechange',function(){
	/*
	Log the State
	*/
	var State = History.getState();
	History.log('statechange:', State.data, State.title, State.url);
	/*
	update the page
	*/
	pageUpdater( State.url, State.data );
});


pageUpdater = function( href, data ) {
	
	document.title=data.data.title;

	/* set the layout to the non layout 
	*  so we dont pull in a whole page 
	*  into part of a page
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
}

/*
clickable ajax links
*/
$(document).on('click', '.ajaxableLink', function(e){

	e.preventDefault();

	/*for things other than links, 
	* this will need updating to 
	* handle data bindings or similar
	*/
	var href = this.href;

	$.get(href, function( data ){

		History.pushState(data, '', href);
		
	});
});