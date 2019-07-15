$(document).ready(function() {

    /**function to start close messages content*/
    $('.message .close')
        .on('click', function() {
            $(this)
                .closest('.message')
                .transition('fade');
        });
    /**function to start tabs */
    $('.menu .item').tab();

    $('select.dropdown').dropdown();

});