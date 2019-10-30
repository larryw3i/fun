(function(){
    var file_field_id = document.querySelector('.preview-file').dataset.fileFieldId;
    if(file_field_id){
        var file_field = document.querySelector( file_field_id );
        var preview_target = document.querySelector('.preview-file').dataset.previewTarget;
        file_field.addEventListener('change',()=>{
            var file = file_field.files[0];
            var file_type = String(file.type);
            if(file_type.startsWith('video/') || file_type.endsWith('/pdf')){
                var reader  = new FileReader();
                reader.onload=function(){
                    var src = this.result
                    document.querySelector(preview_target).innerHTML='<hr/>'+(
                        file_type.startsWith('video/')?
                        `<video src="${src}" controls="controls" class='mh-80 w-100'></video>`:
                        `<object data='${src}'  type=${file_type} height='560px' class=' w-100'></object>`)
                }
                reader.readAsDataURL(file);
            }
            
        })
    }
})();