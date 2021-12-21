$(document).ready(function(){
    $img = $('.img-child')
        $img.each(function(e){
            $(this).click(function(evt){
                evt.preventDefault();
                $img_show = $('#img-show')
                $img_show.attr('src', '')
                let src = $(this).attr('value')
                $img_show.attr('src', src)
    
            })
    
        })
    
    })
    