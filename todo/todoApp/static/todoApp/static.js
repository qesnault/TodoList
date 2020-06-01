$(document).ready(function () {
    $('input[name=realise]').change(function () {
        $(this).closest("form").submit();
    });
});