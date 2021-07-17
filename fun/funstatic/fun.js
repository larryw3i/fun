
////// COMMON

function checkCookies(){
    if( Cookies.get('read_privacy') == undefined ){
        makeGlobalAlert(
            gettext("Read our Privacy & Cookies")+
            `  <button type="button" class="btn btn-info" add-privacy-cookies `+
            `data-url='/data_privacy'>`+gettext("Read Privacy & Cookies")+
            `&gt;&gt;</button>`,
            60*60
        )
    }
}

/**
 * Make a global alert
 * @param {String} message message
 * @param {number} timeout in second
 * @param {String} type Bootstrap alert
 */
function makeGlobalAlert( message='Hello',timeout=2.5, type='info' )
{
    $(`<div class="text-center rounded global-alert alert-${type}" role="alert">
        ${message}</div>`)
        .prependTo('body');

    setTimeout(()=>{
        $('.global-alert').remove();
    }, timeout*1000);
}

/** 
 * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
 */
function refreshLabelList( event )
{
    is_my_label_list = Boolean( Cookies.get('is_my_label_list') );
    Cookies.set(
        'is_my_label_list' ,
        is_my_label_list?'':'1' , { expires: 365 } );
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
        'data':'/static/pdf.js/web/viewer.html?file='
            + URL.createObjectURL( event.target.files[0] )
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
        $(`img[preview-for='#${event.target.id}']`)
            .attr( {'src': this.result });
    }
    fileReader.readAsDataURL(event.target.files[0])
}

(function(){

    checkCookies();

    // deprecated
    /////////
    $(document).on('change', `input[type='file'].preview-image`, (event)=> {
        previewImage(event);
    });

    $(document).on('change', `input[type='file'].preview-pdf`, (event)=> {
        previewPdf(event);
    });

    $(document).on('change', `input[type='file'].preview-video`, (event)=> {
        previewVideo(event);
    });
    /////////

    $(document).on('click', `.theme-dropdown-menu a` , (event) =>{
        changeTheme(event);
    });

    $(document).on('click', `#id_label_list_view_mine_only` , (event) =>{
        refreshLabelList(event);
    });
    
    $(document).on('click', `.language-dropdown-menu .language-dropdown-item` , 
        (event) =>{
        $(`#language_form input[name='language']`)
            .val(event.target.dataset.language);
            $(`#language_form`).trigger('submit');
    });

    $(document).on('click', `[add-privacy-cookies]` , (event) =>{
        Cookies.set('read_privacy','1');
        privacy_url = event.currentTarget.dataset.url;
        $('.global-alert').remove();
        window.location = privacy_url;
    });

    $(document).on('click', `[click-to]` , (event) =>{
        $(`${$(event.currentTarget).attr('click-to')}`).trigger('focus');
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

    if( $('.beian_text').text().trim().length < 1 ) $('.beian_text').remove();

})();
