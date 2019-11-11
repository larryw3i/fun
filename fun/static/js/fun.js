(function(){
    $(document).on('change', `input[type='file'].preview-image`, (event)=> {
        previewImage(event);
    })

    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function previewImage(event){
        console.log(event.target.id)
        var fileReader = new FileReader();
        fileReader.onload = function(){
            $(`img[preview-for='#${event.target.id}']`).attr( {'src': this.result });
        }
        fileReader.readAsDataURL(event.target.files[0])
    }

})();