(function(){
    /*
    $(document).on('change', $(`input[type='file'] .preview`), ()=>{

    })
    if($(`input[type='file']`).hasClass('preview'))
    {
        var file_input = $(`input[type='file']`);
        var file_input_id = file_input.attr('id');
        file_input.on('change',()=>{
            var reader = new FileReader();
            var file = document.getElementById(file_input_id).files[0] ;
            let html = ''

            if(String(file.name).endsWith('.pdf')){
                
                html = `<hr/><object data='${window.URL.createObjectURL(file)}' type='${file.type}' class='w-100' height='560px'></object>`
                $(`[preview-for='${file_input_id}']`).html( html ); 
            }
            else if(String(file.type).startsWith('video/') ){
                
                html = `<hr/><video src='${window.URL.createObjectURL(file)}' controls class='w-100 mh-100'></video>`
                $(`[preview-for='${file_input_id}']`).html( html ); 
                
            }

        })
    }
    */

})();