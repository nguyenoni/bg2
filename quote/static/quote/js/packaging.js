
// load more product
$('.load-more').click(function (e) {
    e.preventDefault();
    let offset = $('.product-item').length;
    let limit = $(this).attr('data-limit');
    let dt = get_value_filter();
    
    if (dt.volume === "" || dt.category ==="") {
        dt.offset = offset
        dt.limit = limit
        let res = request("GET", "api/load-more-packaging/", dt)
        if (res.error == false) {
            $('.list-product').append(res.data);
            if (res.has_page == false) {
                $('.load-more').addClass('hide')
            }
        }
        else {
            show_mess(res.message)
        }
    }
    else {
        load_dt(e, offset, limit)
    }

})

function load_dt(e, offset, limit) {
    e.preventDefault();
    let dt = get_value_filter();
    dt.offset = offset;
    dt.limit = limit;
    dt.csrfmiddlewaretoken = get_csrfmiddlewaretoken();

    let res = request("POST", 'api/load-more-packaging/', dt)
    if (res.error == false) {
        if (res.no_data == true) {
            $('.list-product').append(res.message);
        } else {
            $('.list-product').append(res.data);
        }

        $('.load-more').attr("data-total", res.total_data);
        $('.load-more').attr("data-limit", res.limit_page);

        if (res.has_page == false) {
            $('.load-more').addClass('hide');
        }
        else {
            $('.load-more').removeClass('hide');
        }
    }
    else {
        show_mess(res.message)
    }
}
// Get value Filter select
function get_value_filter(){
    return {
        "category": $('.category').children("option:selected").val(),
        "volume": $('.volume').children("option:selected").val(),
    }
}
// when select product
$('select.volume').change(function (e) {

    // e.stopImmediatePropagation();
    e.preventDefault();
    let selected = $(this).children("option:selected").val();
    if (selected !== null) {
        let dt = get_value_filter();
        dt.csrfmiddlewaretoken = get_csrfmiddlewaretoken();
        let res = request("POST", 'bao-bi', dt)
        if (res.no_data == true) {

        }
        if (res.error == false) {
            $('.list-product').empty();

            if (res.no_data == true) {
                $('.list-product').append(res.message);
            } else {
                $('.list-product').append(res.data);
            }

            $('.load-more').attr("data-total", res.total_data);
            $('.load-more').attr("data-limit", res.limit_page);

            if (res.has_page == false) {
                $('.load-more').addClass('hide');
            }
            else {
                $('.load-more').removeClass('hide');
            }
        }
        else {
            show_mess(res.message)
        }
        
    }

})

// when select category
// when select product
$('select.category').change(function (e) {

    // e.stopImmediatePropagation();
    e.preventDefault();
    let dt = get_value_filter();
    if (dt.category !== null) {
        
        dt.csrfmiddlewaretoken = get_csrfmiddlewaretoken();
        let res = request("POST", 'bao-bi', dt)
        if (res.no_data == true) {

        }
        if (res.error == false) {
            $('.list-product').empty();

            if (res.no_data == true) {
                $('.list-product').append(res.message);
            } else {
                $('.list-product').append(res.data);
            }

            $('.load-more').attr("data-total", res.total_data);
            $('.load-more').attr("data-limit", res.limit_page);

            if (res.has_page == false) {
                $('.load-more').addClass('hide');
            }
            else {
                $('.load-more').removeClass('hide');
            }
        }
        else {
            show_mess(res.message)
        }
        
    }

})
