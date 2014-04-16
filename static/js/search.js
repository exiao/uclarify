$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "/ajax/search/",
        //data: send_data,
        success: function(response){
            $("#analysts").html(response["analyst_page"]);
        }
    });
})