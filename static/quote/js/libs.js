function get_csrfmiddlewaretoken() {
	return $(".no-s").attr('val');
}
function request(type,slug,dict){
    
    let res = $.ajax({
            type: type,
            url: slug,
            dataType: 'json',
            data: dict,
            async: false,
        });

    return JSON.parse(res.responseText)
}
function show_mess(mess, tp){
    if(tp === ERR){

        toastr.error(mess)
    }
    else{
        toastr.success(mess);
    }
}

function truncate(str, no_words) {
    let result = str;
    if(no_words < str.length){
        result = str.split(" ").splice(0,no_words).join(" ").concat(" ...");
    }
    return result
}

function hide_modal(){
    $(".modal").modal("hide");
}

const MATERIAL = "MATERIAL";
const PACKAGINGLEVEL1 = "PACKAGINGLEVEL1";
const PACKAGINGLEVEL2 = "PACKAGINGLEVEL2";
const STAMP = "STAMP";
const PACKINGWORKER = "PACKINGWORKER";
const ANNOUNCED = "ANNOUNCED";
const FEESHIP = "FEESHIP";
const ERR = "ERROR";

const LIST_MATERIAL = "list_material"
const LIST_PACKAGINGLEVEL1 = "list_packaging_level1";
const LIST_PACKAGINGLEVEL2 = "list_packaging_level2";
const LIST_STAMP = "list_stamp";
const LIST_PACKINGWORKER = "list_packingworker";
const LIST_ANNOUNCED = "list_announced";
const LIST_FEESHIP = "list_feeship";

