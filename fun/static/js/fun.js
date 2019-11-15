(function(){
    $(document).ready(()=>{
        
    });

    $(document).on('change', `input[type='file'].preview-image`, (event)=> {
        previewImage(event);
    });

    $(document).on('change', `input[type='file'].preview-pdf`, (event)=> {
        previewPdf(event);
    });

    $(document).on('click', `.theme-dropdown-menu a` , (event) =>{
        changeTheme(event);
    });

    $(document).on('click', `.label_card` , (event) =>{
        window.location = event.currentTarget.dataset.url;
    });


    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function previewPdf(event){
        var fileReader = new FileReader();
        fileReader.onload = function(){
            $(`object[preview-for='#${event.target.id}']`).attr( {'data': this.result });
        }
        fileReader.readAsDataURL(event.target.files[0])
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