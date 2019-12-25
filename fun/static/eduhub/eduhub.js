
(function(){
    
	$(document).on( 'click', '#eduhubTopFilterDropdownMenu a', (event)=>{
        var  filter_label = $(event.currentTarget).data('filter_label');
        Cookies.set('eduhub_top_filter' , filter_label , {'expires': 365 });
        location.reload();
    } );
	$(document).on( 'click', '#eduhub_search_submit', (event)=>{
        event.preventDefault();
        if( $(`#eduhub_search_q`).val().length >0 )
        {
            $(`#eduhub_search_form`).submit();
        }
    } );

    $(document).on('click', '.eduhub_search_filter', (event)=>{
        var urlsearch = new URLSearchParams( location.search );
        if( $(event.currentTarget ).hasClass('labels') )
        {
            urlsearch.set( 'filter', 'labels' );
        }
        else
        {
            urlsearch.set( 'filter', 'funcontents' );
        }
        location.href = location.pathname +"?"+urlsearch.toString();
    });
}());
