$(document).ready(function(){
    let button = $('button')
    button.click(function(){
        $('#result').empty()
        let num = $(this).attr('value');
        for(let i=1; i<10;i++){
            $('#result').append('<p>'+num+'*'+i+"="+num*i+'</p>');
        }

    })
})