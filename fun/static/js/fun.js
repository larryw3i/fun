(function(){
    $(document).ready(()=>{
        insertThemeDropdownItems()
    });
    $(document).on('change', `input[type='file'].preview-image`, (event)=> {
        previewImage(event);
    });

    function insertThemeDropdownItems(){
        $.get(`/get_dropdown_items`, (dropdown_items) =>{
            $(`[aria-labelledby='themeDropdown']`).append(dropdown_items);
        })

    }
    
    $(document).on('click', `.theme-dropdown-menu a` , (event) =>{
        changeTheme(event);
    });

    /**
     * 
     * @param { JQuery.ChangeEvent<Document, undefined, any, any> } event 
     */
    function changeTheme(event){
        Cookies.set('theme', event.target.dataset.theme);
        location.reload();
    }

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