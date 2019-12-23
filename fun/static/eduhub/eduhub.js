
(function(){
    $.get('/eduhub/eduhub_navbar_content', (response)=>{
        $('#eduhubNavbarContent').append(response);
    });
}());
