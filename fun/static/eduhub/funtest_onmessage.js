

(function(){

    var message_data = 
`AAAAAAAA
aaaaaaaaaa
aaaAAAaaa
# AAAABBBVfffdd
## DVKJHJKSDHKLAHGAKLGHAKGHFK AN
A. DKJFH AKFH ALF 
B. HK HALFH
C. HKJFGH L
D. dsjfla hf
## aaaaaaaDVKJHJKSDHKLAHGAKLGHAKGHFK AN
A. DKJFH AaaKFH ALF 
B. HK HALFHaa
C. HKJFGH Laaa
D. dsjfla hfaa

#  AAAABBBVVVVff
## sdfjasdfjafjda fda jflajfda
A. DKJFH AKFH ALF 
B. HK HALFH
C. HKJFGH L
D. dsjfla hf

# AAAABBBVVVVss
#  AAAABBBVVVbbb
`;

    var test_type_template = ( test_num, test_tip )=> `
    <h5>${ test_num }. ${test_tip}</h5>
    `;
    var test_template = ( test_num, test )=> `
    <h6 style='margin-left:10px;'>${ test_num }. ${test}</h6>
    `;


    var pre_title = message_data.split('\n')[0];
    var title = message_data.split('\n')[1];
    var last_title = message_data.split('\n')[2];

    var test_type_pattern = /\n#\s+/g

    test_types = message_data.split( test_type_pattern );
    test_types = test_types.slice( 1 , test_types.length );

    var global_index = 1;
    
    test_types_html = '';
    test_types.forEach( (value, index, array)=>{
        test_types_html += test_type_template( index+1, 
        value.split('\n')[0] );
        test_questions = value.split( /\n##\s+/g );
        test_questions = test_questions.slice(1 , test_questions.length );
        test_questions.forEach( (value, index, array )=>{
            test_types_html += test_template( global_index , 
                value.split('\n')[0]);
            global_index++;
        });

    });

    $('#test_body').html( test_types_html );

    $('#pre_title').text( pre_title );
    $('#title').text( title );
    $('#last_title').text( last_title );
    

    
}());


// (function(){

//     var test_type_template = ( test_num, test_tip )=> `
//         <h5>${ test_num }. ${test_tip}</h5>
//     `;
//     var funtest_text_bc = new BroadcastChannel('funtest_text_bc');
//     funtest_text_bc.onmessage = function( message ){
//         var message_data = message.data;

//         var pre_title = message_data.split('\n')[0];
//         var title = message_data.split('\n')[1];
//         var last_title = message_data.split('\n')[2];


//         $('#pre_title').text( pre_title );
//         $('#title').text( title );
//         $('#last_title').text( last_title );
//     }

//     window.onunload = function(){
//         Cookies.remove('is_living');
//     }
    
// }());
