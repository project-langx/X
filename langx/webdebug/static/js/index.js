$(document).ready(function() {

    $("#generate_tokens").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/generate-tokens", data, swal_ajax_post_redirect);
    })

    $("#generate_ast").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/generate-ast", data, swal_ajax_post_redirect);
    });

    $("#generate_bytecode").click(function() {
        let data = {"file_path": ["empty"]};
        validate_and_post("/generate-bytecode", data, swal_ajax_post_redirect);
    });

});