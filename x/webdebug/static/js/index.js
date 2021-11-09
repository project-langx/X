$(document).ready(function() {

    $("#debug").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/debug", data, simple_ajax_post_redirect);
    });

});