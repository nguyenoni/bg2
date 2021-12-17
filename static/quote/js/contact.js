$('.btn-send').click(function(e){
    e.preventDefault();
    let name = $('.name').val();
    let phone = $('.phone').val();
    let email = $('.email').val();
    let content = $('textarea#content').val();
    $('.overlay').css("display", "block");
    dt={
        "name": name,
        "email": email,
        "phone": phone,
        "content": content,
        "csrfmiddlewaretoken": get_csrfmiddlewaretoken(),
    }
    console.log(dt);
    $.ajax({
        type: 'POST',
        url: '/lien-he',
        dataType: 'json',
        data: dt,
        success: function (res) {
            $('.overlay').css("display", "none");
            if (res.error == false) {
                // $('.list-product').empty();
                show_mess(res.message)
                $('.name').val("");
                $('.phone').val("");
                $('.email').val("");
                $('textarea#content').val("");
            }
            else {
                show_mess(res.message, ERR)
            }
        }

    })

})