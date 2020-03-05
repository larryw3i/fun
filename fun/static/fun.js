
////// COMMON


(function(){

    $(document).on('change', `input[type='file'].preview-image`, (event)=> {
        previewImage(event);
    });

    $(document).on('change', `input[type='file'].preview-pdf`, (event)=> {
        previewPdf(event);
    });

    $(document).on('change', `input[type='file'].preview-video`, (event)=> {
        previewVideo(event);
    });

    $(document).on('click', `.theme-dropdown-menu a` , (event) =>{
        changeTheme(event);
    });

    $(document).on('click', `#id_label_list_view_mine_only` , (event) =>{
        refreshLabelList(event);
    });
    
    $(document).on('click', `.language-dropdown-menu .language-dropdown-item` , (event) =>{
        $(`#language_form input[name='language']`).val(event.target.dataset.language); $(`#language_form`).submit();
    });
    $(document).on('click', `[click-to]` , (event) =>{
        $(`${$(event.currentTarget).attr('click-to')}`).click();
    });
    

    $(document).on('click', `.eduhub-label-card` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });

    $(document).on('click', `.eduhub-label-card` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });
 
    $(document).on('click', `.click-to-url` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });
    
    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function refreshLabelList( event )
    {
        is_label_list_mine = Boolean( Cookies.get('is_label_list_mine') );
        Cookies.set( 'is_label_list_mine' , is_label_list_mine?'':'1' , { expires: 365 } );
        location.reload();
    }

    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function previewVideo(event){
        var preview_for =  $(`video[preview-for='#${event.target.id}']`) ;
        if( ! String(event.target.files[0].type).startsWith('video/') ){
            preview_for.removeAttr('src');
            preview_for.hide();
            return;
        }
        preview_for.show();
        preview_for.attr( {
            'src': URL.createObjectURL( event.target.files[0] )
        });
 
    }


    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function previewPdf(event){
        var preview_for =$(`object[preview-for='#${event.target.id}']`);
        if( ! String(event.target.files[0].type).endsWith('/pdf') ) {
            preview_for.removeAttr('data');
            preview_for.hide();
            return;
        }
        preview_for.show();
        preview_for.attr( {
            'data':'/static/libs/pdfjs-2.2.228-dist/web/viewer.min.html?file='+ URL.createObjectURL( event.target.files[0] ) 
        });
 
    }

 

    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function changeTheme(event){
        Cookies.set(
            'theme', 
            event.target.dataset.theme,
            { expires: 365 } ); 
        location.reload();
    }

    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function previewImage(event){
        var fileReader = new FileReader();
        fileReader.onload = function(){
            $(`img[preview-for='#${event.target.id}']`).attr( {'src': this.result });
        }
        fileReader.readAsDataURL(event.target.files[0])
    }

})();

/**
 * Make a global alert
 * @param {String} message message
 * @param {String} type Bootstrap alert, view it https://getbootstrap.com/docs/4.4/components/alerts/#examples 
 */
function makeGlobalAlert( message='Hello',timeout=2500, type='info' )
{
    $(`<div class="text-center rounded alert alert-${type}" role="alert">${message}</div>`).prependTo('body');
    setTimeout(()=>{
        $('.alert').remove();
    }, timeout);
}