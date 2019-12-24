
(function(){
    
	$(document).on( 'click', '#eduhubTopFilterDropdownMenu a', (event)=>{
        var  filter_label = $(event.currentTarget).data('filter_label');
        console.log( filter_label );
        Cookies.set('eduhub_top_filter' , filter_label );
        location.reload();
    } );
	$(document).on( 'click', '#eduhub_search_submit', (event)=>{
        event.preventDefault();
        if( $(`#eduhub_search_q`).val().length >0 )
        {
            $(`#eduhub_search_form`).submit();
        }
    } );
}());
