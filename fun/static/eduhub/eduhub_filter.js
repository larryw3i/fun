
(function(){
	var eduhub_filter = Cookies.get('eduhub_filter');
	if(eduhub_filter.length > 0)
	{
		let eduhub_filters = eduhub_filter.split(';');
		if(eduhub_filters[0].length > 0)
		{
			var eduhub_filter_top = $(`.top-filter button:contains('${eduhub_filters[0]}')`);

			eduhub_filter_top.show();
		} 
		if(eduhub_filters[1].length > 0){
			var eduhub_filter_second = $(`.se-filter button:contains('${eduhub_filters[0]}')`);
			eduhub_filter_second.show();
		} 
		if(eduhub_filters[2].length > 0){
			var eduhub_filter_third = $(`.top-filter button:contains('${eduhub_filters[0]}')`);
			eduhub_filter_third.show();
		} 
	}
}());
