
$('.create-quote-pdf').click(function (e) {
    e.preventDefault();
    let product = $('.change-val').attr("valp");
    let volume = $('.change-val').attr("valv");
    let quantity = $('.quantity').val();
    let material = JSON.parse(localStorage.getItem("material"))
    let packaging_level1 = JSON.parse(localStorage.getItem("packaging-level1"))
    let packaging_level2 = JSON.parse(localStorage.getItem("packaging-level2"))
    let stamp = JSON.parse(localStorage.getItem("stamp"))
    let packing_worker = JSON.parse(localStorage.getItem("packing-worker"))
    let announced = JSON.parse(localStorage.getItem("announced"))
    let feeship = JSON.parse(localStorage.getItem("feeship"))


    if(packaging_level1 == undefined){
        packaging_level1 = 0;
    }
    if(packaging_level2 == undefined){
        packaging_level2 = 0;
    }
    if(feeship == undefined){
        feeship = 0
    }
    if(stamp == undefined){
        stamp = 0
    }
    
    if($('select.product').children("option:selected").val() == ""){
        show_mess("Vui lòng chọn sản phẩm!", ERR);
    }
    else if($('select.volume').children("option:selected").val() == ""){
        show_mess("Vui lòng chọn dung tích sản phẩm!", ERR);
    }
    else if(quantity == ""){
        show_mess("Vui lòng nhập số lượng sản phẩm cần gia công!", ERR);
    }
    else if(material == null){
        show_mess("Vui lòng chọn nguyên liệu!", ERR);
    }
    else if(packing_worker == null){
        show_mess("Vui lòng chọn nhân công đóng gói!", ERR);
    }
    else if(announced == null){
        show_mess("Vui lòng chọn gói công bố kiểm nghiệm!", ERR);
    }
    else {
        packaging_level1 =  (packaging_level1 ==0)? packaging_level1.toString() : packaging_level1.key.toString();
        packaging_level2 = (packaging_level2 ==0)? packaging_level2.toString() : packaging_level2.key.toString();
        stamp = (stamp == 0)?stamp.toString():stamp.key.toString();
        feeship = (feeship==0)?feeship.toString():feeship.key.toString();
        const param = `${product}-${volume}-${material.key}-${packaging_level1}-${packaging_level2}-${stamp}-${packing_worker.key}-${announced.key}-${feeship}-${quantity}`;
        
        let dt = {
            "slug": param,
            'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
        }
        res = request("POST", '/api/get-param/',dt)
 
        if(res.error == false){
            let url = `/export-pdf/${res.data.url}`;
            window.open(url);
        }
        else{
            show_mess(res.message, ERR);
        }
    }

})