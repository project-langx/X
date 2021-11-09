$(document).ready(function() {

    $("#generate_tokens").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/generate-tokens", data, simple_ajax_post_redirect);
    })

    $("#generate_ast").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/generate-ast", data, simple_ajax_post_redirect);
    });

});