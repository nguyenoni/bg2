
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
    let url = ``;

    // console.log(volume, product, material, packaging_level1, packaging_level2, stamp, packing_worker, announced, feeship)
    if(quantity == ""){
        show_mess("Vui lòng nhập số lượng sản phẩm cần gia công!", ERR);
    }
    if (material !== null && volume !== null && product !== null && packaging_level1 !== null && packaging_level2 !== null && stamp !== null
        && packing_worker !== null && announced !== null && feeship !== null) {
        url = `/export-pdf/${product}/${volume}/${material.key}/${packaging_level1.key}/${packaging_level2.key}/${stamp.key}/${packing_worker.key}/${announced.key}/${feeship.key}/${quantity}`
        window.open(url)

    }
    else {
        show_mess("Vui lòng chọn đầy đủ các trường để hoàn tất báo giá!", ERR);
    }
    // let url = "http://127.0.0.1:8000/export-pdf/UADV/UADP";

})