$(document).ready(function(){
    let nav = $('ul');
    let staticTop = $('.staticTop').offset().top

    $(window).on('scroll',function(e){
        if($(window).scrollTop()>staticTop){
            nav.addClass('fixed')
        } else {
            nav.removeClass('fixed')
        }
    })
    
})