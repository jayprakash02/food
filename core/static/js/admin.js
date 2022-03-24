window.onload=function(){
    $(".field-image").append("<a id='prev' onclick='Preview()'>Preview</a>")
    $("#prev").css('cursor','pointer')
    checkUser()
    
}
function Preview(){
    var url=$('#id_image').val();
    $.get(url)
    .done(function() { 
        $(".field-image").append("<img src='"+url+"' /> ");
    }).fail(function() { 
        alert('Image Not Found')
    })
}
function checkImage(url) {
    var request = new XMLHttpRequest();
    request.open("GET", url, true);
    request.send();
    request.onload = function() {
        status = request.status;
        if (request.statusText == 'OK') //if(statusText == OK)
        {
            return true;
        } else {
            return false;
        }
    }
}

checkUser = async()=> {
    var request = new XMLHttpRequest();
    request.open("GET", 'http://127.0.0.1:8000/utils/', true);
    request.send();
    request.onload = function() {
        status = request.status;
        if (request.statusText == 'OK') //if(statusText == OK)
        {
            var id=JSON.parse(request.response).user
            $("#id_approved_by").val( id).change()
            $('#id_approved_by option')
            .each(function() {
                if ( $(this).val() != id ) {
                    $(this).remove();
                }
            })
            //$("#id_approved_by").attr('disabled','disabled');
        }
    }
}