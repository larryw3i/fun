
(function(){
    if($('#id_classification'))
    {
        $('#id_classification').editableSelect();
        if( $(`#div_id_classification li:first`).is(`[selected]`) )
        {
            $('#id_classification').val('')
        }
    }
})();