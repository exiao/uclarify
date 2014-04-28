$(document).ready(function () {
    var current_type = "analyst-type"; //analyst-type, analyst-firm-type -- these values are the ID of the button
    var sort_option = "relevance";

    //activate the initial type
    activateType(current_type);

    //switches the current type in the front end(analyst, analyst firm)
    $(".type-btn").click(function () {
        //handle button logic
        current_type = $(this).attr("id");
        $(".type-btn").removeClass("active");
        $(this).addClass("active");
        activateType(current_type);
    });

    runSearch(); //run search once when page loads

    $("#sidebar-form").submit(function () {
        event.preventDefault(); //stop search redirecting the whole page
        runSearch();
    });

    $("#cancel-query").click(function () {
        $("#query-id").val("");
        runSearch();
    });

    //run search when you hit a specialization filter
    $("#specialization-id").change(function () {
        runSearch();
    });

    //change sort option
    $(".sort-option").on("click", function () {
        if (!$(this).hasClass("active")) {
            $(".sort-option").removeClass("active");
            $(this).addClass("active");
            sort_option = $(this).attr("id");
            runSearch();
        }
    });

    function runSearch() {
        showLoading(true);
        var url = $("#sidebar-form").attr("action");
        $.ajax({
                   type: "GET",
                   url: url,
                   data: $("#sidebar-form").serialize() + "&sort=" + sort_option,
                   success: function (response) {
                       $("#analysts").html(response["analyst_page"]);
                       $("#analyst-firms").html(response["analyst_firm_page"]);

                       $(".analyst-number").html(response["analyst_number"]);
                       $(".analyst-firm-number").html(response["analyst_firm_number"]);

                       //if query exists, show the "search results for" section
                       if ($("#query-id").val()) {
                           $("#results-for").show();
                           $("#results-for-query").html($("#query-id").val());
                           $("#cancel-query").show()
                       } else {
                           $("#results-for").hide();
                           $("#cancel-query").hide()
                       }


                   }
               }).done(function () {
                           showLoading(false);
                       });
    }
});


/**
 * Shows all the matching type classes while hiding the inactive ones
 * Under the assumption that all type based objects(the results list, filter elements, etc) will have "type" in the class
 * @param type - analyst-type, analyst-firm-type, etc
 */
function activateType(type) {
    $(".type").each(function (index) {
        if ($(this).hasClass(type)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

/**
 * shows ajax loader screen
 * show - boolean
 */
function showLoading(show) {
    if (show) {
        $("#loading-screen").show();
        $("#ajax-loader").show();
    } else {
        $("#loading-screen").hide();
        $("#ajax-loader").hide();
    }
}