(function(){
    $(document).ready(()=>{
        setTimeZone();
    });

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
    
    $(document).on('click', `.language-dropdown-menu .language-dropdown-item` , (event) =>{
        $(`#language_form input[name='language']`).val(event.target.dataset.language);
        $(`#language_form`).submit();
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

    function setTimeZone()
    {
        if ( ( ! Cookies.get('timezone')) && navigator.cookieEnabled )
        {

            Cookies.set( 
                'timezone' , 
                Intl.DateTimeFormat().resolvedOptions().timeZone ,
                { expires: 365 }); 
            if( Cookies.get('timezone') ) location.reload();  
            
        }
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