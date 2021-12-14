window.onload = function() {
    localStorage.clear();
  };
function show_mess(mess,tp=""){
   
    if(tp === ERR){
        toastr.error(mess);
    }
    else{
        toastr.success(mess);
    }
}
// when select product
    $('select.product').change(function (e) {

        // e.stopImmediatePropagation();
        e.preventDefault();
         let selected = $(this).children("option:selected").val()
 
         dt = {
             'unique_product': selected,
             'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
         }
         $.ajax({
            type: 'POST',
            url: '/api/load-volume-product/',
            dataType: 'json',
            data: dt,
            success: function(data){
                if(data.data.status==200){
                    show_mess(data.data.message)
                    arr_dt = data.data.data
                    $volume = $('select.volume')
                    $volume.children().remove();
                    $volume.append($.parseHTML(`<option value="">--Chọn dung tích--</option>`))
                    arr_dt.map(item=>{
                        $volume.append($.parseHTML(`<option value="${item.unique_volume}">${item.name}</option>`))
                    })
                }
                else{
                    show_mess(data.data.message)
                }


            }


        })
    })

// when select volume
$('select.volume').change(function(e){
    // e.preventDefault();
    let valv = $(this).children("option:selected").val();
    let valp = $('select.product').children("option:selected").val();
    $('.change-val').attr("valp",valp)
    $('.change-val').attr("valv",valv)

})

// Show titile modal
function show_title_modal(tt){
    let title = $('.modal-title');
    title.text("");
    title.text(tt);
}

// Show data in modal

function show_data_to_table(data, act){
    show_title_modal(data.title);
    arr_dt = data.data
    if(arr_dt){
        
        let data_show = $('.data-show');
        data_show.empty();
        arr_dt.map((item, index)=>{
            let tr = `<tr>
                    <th scope="row">${index+1}</th> 
                    <!-- <th><img src="assets/images/avatar1.png" style="width: 60px;" /></th> -->
                    <th>${item.name}</th>
                    <td class="text-success"><b>${item.price}</b> <sup>vnđ</sup></td>
                    <th>${item.note}</th>
                    <th><span class="btn btn-success btn-xs add-to-quote" onclick="add_to_qoute(${item.key}, '${item.name}', ${item.price}, '${item.note}', '${act}')">Thêm vào báo giá</span></th>
                </tr>`
            data_show.append(tr);
        })
    }
}

// When button click choose material
$('.material').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv")
    let valp = $('.change-val').attr("valp")

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-material/',
       dataType: 'json',
       data: dt,
       success: function(data){
           if(data.data.status==200){
            //    show_mess(data.data.message)
               arr_dt = data.data.data
               show_data_to_table(data.data, MATERIAL)
           }
           else{
               show_mess(data.data.message)
           }
       }

   })


})

// Event click to add-to-quote
// $('.add-to-quote').click(function(e){
//     dataLayer.push({ 'event': 'button1-click' });
// })
// Function add to qoute when click in set item to quote
function add_to_qoute(key, name, price, note, action){
    data = {
        "key":key,
        "name": name,
        "price": price,
        "note": note
    }
    if(action ===MATERIAL){
        // Add data choose to row in qoute page
        add_data_to_row_quote(data, 'material');
        show_mess("Đã thêm nguyên liệu vào báo giá");
    }
    else if(action === PACKAGINGLEVEL1){
        add_data_to_row_quote(data, 'packaging-level1');
        show_mess("Đã thêm bao bì cấp 1 vào báo giá");
    }
    else if(action === PACKAGINGLEVEL2){
        add_data_to_row_quote(data, 'packaging-level2');
        show_mess("Đã thêm bao bì cấp 2 vào báo giá");
    }
    else if(action === STAMP){
        add_data_to_row_quote(data, 'stamp');
        show_mess("Đã thêm tem nhãn vào báo giá");
    }
    else if(action === PACKINGWORKER){
        add_data_to_row_quote(data, 'packing-worker');
        show_mess("Đã thêm nhân công đóng gói vào báo giá");
    }
    else if(action === ANNOUNCED){
        add_data_to_row_quote(data, 'announced');
        show_mess("Đã thêm gói công bố kiểm nghiệm vào báo giá");
    }
    else if(action === FEESHIP){
        add_data_to_row_quote(data, 'feeship');
        show_mess("Đã thêm gói vận chuyển vào báo giá");
    }
    
}
// update total
function update_total(){
    let total = 0;
    
    let material = parseInt($(".material-price>b").text());
    let packaging_level1 = parseInt($(".packaging-level1-price>b").text());
    let packaging_level2 = parseInt($(".packaging-level2-price>b").text());
    let packing_worker = parseInt($(".packing-worker-price>b").text());
    let stamp = parseInt($(".stamp-price>b").text());
    let announced = parseInt($(".announced-price>b").text());
    let feeship = parseInt($(".feeship-price>b").text());

    // console.log(packaging_level1)
    
    if(!isNaN(material)){
        total+=material;
    }if(!isNaN(packaging_level1)){
        total+=packaging_level1;
    }
    if(!isNaN(packaging_level2)){
        total+=packaging_level2;
    }
    if(!isNaN(packing_worker)){
        total+=packing_worker;
    }
    if(!isNaN(stamp)){
        total+=stamp;
    }
    if(!isNaN(announced)){
        total+=announced;
    }
    if(!isNaN(feeship)){
        total+=feeship;
    }

    $('.total-tt').removeClass('hide');
    $('.total-price').removeClass('hide');
    $('.total-title').removeClass('hide');

    $('.total-price').empty();
    $('.total-price').append($.parseHTML(`<b>${total.toLocaleString("fi-FI")}</b> <sup>vnđ</sup>`));
    
    
    localStorage.removeItem("total");
    localStorage.setItem("total", total);

    if(total == 0){
        $('.total-tt').addClass('hide');
        $('.total-price').addClass('hide');
        $('.total-title').addClass('hide');
    }
}
// add data to row
function add_data_to_row_quote(data, class_add_data){
    if(data){
        let type = $('.'+class_add_data+'-type');
        let title = $('.'+class_add_data+'-title');
        let price = $('.'+class_add_data+'-price');
        let btn = $('.'+class_add_data+'-button');
        let act = $('.'+class_add_data+'-action');
        
        title.text("");
        price.text("");

        title.text(data.name);
        price.append($.parseHTML(`<b>${data.price}</b> <sup>vnđ</sup>`));
        // price.text(data.price)

        type.removeClass('hide');
        title.removeClass('hide');
        price.removeClass('hide');
        btn.addClass('hide');
        act.removeClass('hide');

        // Add to localStore
        localStorage.removeItem(class_add_data);
        localStorage.setItem(class_add_data, JSON.stringify(data));
        update_total();
        
    }
}
// event click icon delete in row choose
$('.delete-item').click(function(e){
    
    e.preventDefault();
    let type_del = $(this).attr("type-del");
    // type_del = key class 
    remove_item_choose(type_del);
})
// Delete item chose and remove on localStorage
function remove_item_choose(item){
    localStorage.removeItem(item);
    
    // remove data in row choose
    let type = $('.'+item+'-type')
    let title = $('.'+item+'-title');
    let price = $('.'+item+'-price');
    let btn = $('.'+item+'-button');
    let act = $('.'+item+'-action');

    title.text("");
    price.text("");

    type.addClass('hide');
    title.addClass('hide');
    price.addClass('hide');
    btn.removeClass('hide');
    act.addClass('hide');
    show_mess("Đã xóa lựa chọn khỏi báo giá!");
    update_total();
}

// When button click choose Packaging Level 1
$('.packaging-level1').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-packaging-level1/',
       dataType: 'json',
       data: dt,
       success: function(data){
           if(data.data.status==200){
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, PACKAGINGLEVEL1);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })


})

// When button click choose Packing Level 2
$('.packaging-level2').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-packaging-level2/',
       dataType: 'json',
       data: dt,
       success: function(data){

           if(data.data.status==200){
               
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, PACKAGINGLEVEL2);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })
})

// When button click choose Stamp
$('.stamp').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-stamp/',
       dataType: 'json',
       data: dt,
       success: function(data){

           if(data.data.status==200){
               
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, STAMP);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })
})

// When button click choose Packing Worker
$('.packing-worker').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-packing-worker/',
       dataType: 'json',
       data: dt,
       success: function(data){

           if(data.data.status==200){
               
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, PACKINGWORKER);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })
})


// When button click choose Announced
$('.announced').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-announced/',
       dataType: 'json',
       data: dt,
       success: function(data){

           if(data.data.status==200){
               
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, ANNOUNCED);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })
})

// When button click choose Announced
$('.feeship').click(function(e){
    // e.preventDefault();
    let valv = $('.change-val').attr("valv");
    let valp = $('.change-val').attr("valp");

    dt = {
        'valp': valp,
        'valv': valv,
        'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
    }
    $.ajax({
       type: 'POST',
       url: '/api/load-feeship/',
       dataType: 'json',
       data: dt,
       success: function(data){

           if(data.data.status==200){
               
            //    show_mess(data.data.message)
               arr_dt = data.data.data;
               show_data_to_table(data.data, FEESHIP);
           }
           else{
               show_mess(data.data.message);
           }
       }

   })
})