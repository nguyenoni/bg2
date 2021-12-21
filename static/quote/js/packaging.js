// show detail
function show_detail(key) {

    if (key !== null) {
        let dt = {
            "key": key
        }
        let res = request("GET", "/api/detail-packaging/", dt)
        if (res.error == false) {
            $('.modal-body').empty();
            $('.modal-body').append(res.data);
        }
        else {
            show_mess(res.message, ERR)
        }

    }
}

// load more product
$('.load-more').click(function (e) {
    e.preventDefault();
    let offset = $('.product-item').length;
    let limit = $(this).attr('data-limit');
    let select = $('select.volume').children("option:selected").val();
    if (select == "") {
        dt = {
            "offset": offset,
            "limit": limit
        }
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

    dt = {
        "volume": $('select.volume').children("option:selected").val(),
        "offset": offset,
        "limit": limit,
        "csrfmiddlewaretoken": get_csrfmiddlewaretoken(),
    }

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

// when select product
$('select.volume').change(function (e) {

    // e.stopImmediatePropagation();
    e.preventDefault();
    let selected = $(this).children("option:selected").val();
    if (selected !== null) {
        dt = {
            "volume": selected,
            "csrfmiddlewaretoken": get_csrfmiddlewaretoken(),
        }
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
