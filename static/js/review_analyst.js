$(document).ready(function () {

    $("#overall-rating").raty({
        path: STATIC_URL + "plugins/raty-2.5.2/img",
        size   : 64,
        starOff  : 'star_none.png',
        starOn   : 'star_full.png',
        scoreName: "overall_rating"
    });

    $(".btn").button();

    //analysts array is instantiated in the html template
    $("#autocomplete").chosen({
                                    });

//    $("#review-form").validate({
//        rules: {
//            is_anonymous: "required",
//            content: "required"
//
//        }
//                               });

});