$(document).ready(function(){
    let button = $('button');
    let num = [], method = []
    
    button.click(function(){
        if ($(this).attr('class') == 'num'){
            num.push(parseInt($(this).attr('value')))
            screen_dis($(this))

        }else if($(this).attr('class') == 'op'){

            if($(this).attr('value') == 'clear'){
                num.length = 0;
                method.length = 0 ;
                $('.screen').empty();
            } else if ($(this).attr('value') == '='){
                //사칙연산 구현
                $('.screen').empty();
                $('.screen').append(calcul())
            } else {
                method.push($(this).attr('value'))
                screen_dis($(this))
            }
        }
    })

    function calcul(num, method){
        let result = 0
        for (let i=0, j=o; i<num.length, j<method.length ;i++,j++){
            if(method[j] == "+"){
             result = num[i]+num[i+1] 
             return result  
            }
        }
    }



    function screen_dis(el){
        let screen_text_value = el.attr('value')
        $('.screen').append(screen_text_value)
    }

})