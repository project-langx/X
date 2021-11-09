$(document).ready(function() {

    $("#some-button").click(function() {
        $.ajax({
            url: "/some-url",
            type: "some-type",
            data: {"some-key": "some-value"},
            success: function(result) {
                // Some processing
            }
        });
    });

});