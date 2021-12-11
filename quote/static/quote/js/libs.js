function get_csrfmiddlewaretoken() {
	return $(".no-s").attr('val');
}

function show_mess(mess, tp){
    if(tp === ERR){

        toastr.error(mess)
    }
    else{
        toastr.success(mess);
    }
}

const MATERIAL = "MATERIAL";
const PACKAGINGLEVEL1 = "PACKAGINGLEVEL1";
const PACKAGINGLEVEL2 = "PACKAGINGLEVEL2";
const STAMP = "STAMP";
const PACKINGWORKER = "PACKINGWORKER";
const ANNOUNCED = "ANNOUNCED";
const FEESHIP = "FEESHIP";
const ERR = "ERROR";