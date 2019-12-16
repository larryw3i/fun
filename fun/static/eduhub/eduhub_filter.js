
(function(){


	var _eduhub_filter = Cookies.get('eduhub_filter');
	if(_eduhub_filter.length > 0)
	{
		let eduhub_filters = _eduhub_filter.split(';');
		$('.top-filter button').show();
		$('.second-filter button').show();
		$('.third-filter button').show();
		if(eduhub_filters[0].length>0)$(`#eduhub_filter button:contains('${eduhub_filters[0]}')`).addClass('btn-info');
		if(eduhub_filters[1].length>0)$(`#eduhub_filter button:contains('${eduhub_filters[1]}')`).addClass('btn-info');
		if(eduhub_filters[2].length>0)$(`#eduhub_filter button:contains('${eduhub_filters[2]}')`).addClass('btn-info');
	}
	
	$(document).on('click', '.top-filter button', (event)=>{
		$('.second-filter button').hide();
		if($(event.currentTarget).hasClass('nursery'))
		{
			$('.third-filter').hide();
		}
		else
		{
			$('.third-filter').show();
		}
		Cookies.set('eduhub_filter', $(event.currentTarget).text()+';;');

		var installment = $(event.currentTarget).data('installment');
		$(`.second-filter button[class*=${installment}]`).show();
		$('.top-filter button').removeClass('btn-info');
		$(event.currentTarget).addClass('btn-info');

	});
	$(document).on('click', '.second-filter button', (event)=>{
		
		var eduhub_filters = Cookies.get('eduhub_filter').split(';');
		Cookies.set('eduhub_filter', eduhub_filters[0]+";"+$(event.currentTarget).text()+";"+eduhub_filters[2]);
		$('.second-filter button').removeClass('btn-outline-info');
		$(event.currentTarget).addClass('btn-info');

	});
	$(document).on('click', '.third-filter button', (event)=>{
		
		var eduhub_filters = Cookies.get('eduhub_filter').split(';');
		Cookies.set('eduhub_filter', eduhub_filters[0]+";"+eduhub_filters[1]+";"+$(event.currentTarget).text());
		$('.third-filter button').removeClass('btn-outline-info');
		$(event.currentTarget).addClass('btn-info');

	});
}());
