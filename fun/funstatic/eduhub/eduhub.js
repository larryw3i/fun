
(function(){
    
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
