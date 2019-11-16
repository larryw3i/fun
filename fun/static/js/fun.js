(function(){
    $(document).ready(()=>{
        
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

    $(document).on('click', `.eduhub-label-card` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });

    $(document).on('click', `.eduhub-content-card` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });


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
            'data': URL.createObjectURL( event.target.files[0] ) 
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