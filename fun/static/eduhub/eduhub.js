
(function(){
    
	$(document).on( 'click', '#eduhubTopFilterDropdownMenu a', (event)=>{
        var  filter_label = $(event.currentTarget).data('filter_label');
        console.log( filter_label );
        Cookies.set('eduhub_top_filter' , filter_label );
        location.reload();
    } );
}());
