// when select product
$('select.product').change(function (e) {

    // e.stopImmediatePropagation();
    e.preventDefault();
    let selected = $(this).children("option:selected").val();
    if(selected !== null){
        dt = {
            "cateogry": selected,
            "csrfmiddlewaretoken": get_csrfmiddlewaretoken(),
        }

        $.ajax({
            type: 'POST',
            url: 'san-pham',
            dataType: 'json',
            data: dt,
            success: function(res){
                if(res.no_data == true){

                }
                if(res.error == false){
                    $('.list-product').empty();

                    if(res.no_data == true){
                        $('.list-product').append(res.message);
                    }else{
                        $('.list-product').append(res.data);
                    }
                    
                    
                    $('.load-more').attr("data-total", res.total_data);
                    $('.load-more').attr("data-limit", res.limit_page);

                    if(res.has_page == false){
                        $('.load-more').addClass('hide');
                    }
                    else{
                        $('.load-more').removeClass('hide');
                    }
                }
                else{
                    show_mess(res.message)
                }
    
    
            }
    
    
        })
    }

})
// load more product
$('.load-more').click(function(e){
    e.preventDefault();
    let offset = $('.product-item').length;
    let limit = $(this).attr('data-limit');

    dt = {
        "offset": offset,
        "limit": limit
    }
    $.ajax({
        type: 'GET',
        url: 'api/load-more-product/',
        dataType: 'json',
        data: dt,
        success: function(res){

            if(res.error == false){
                $('.list-product').append(res.data);
                if(res.has_page == false){
                    $('.load-more').addClass('hide')
                }
            }
            else{
                show_mess(res.message)
            }


        }


    })
})

// item btn detail click

// $('.item-btn-detail').click(function(e){
//     e.preventDefault();
//     let url = $(this).attr("valp")
//     console.log(url)
// })
// s
function show_detail(url){
    if(url !== null){
        let dt = {
            "slug": url
        }
        $.ajax({
            type: 'GET',
            url: 'api/detail-product/',
            dataType: 'json',
            data: dt,
            success: function(res){
                
                if(res.error == false){
                    $('.modal-body').empty();
                    $('.modal-body').append(res.data);

                }
                else{
                    show_mess(res.message)
                }
    
    
            }
    
    
        })
    }
}