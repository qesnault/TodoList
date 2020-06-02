function countChar(val, max) {
    var len = val.value.length;
    if(len >= (max/1.25)){
        $('#charNum').text(max - len);
        $('#charNum').show("fast");
    } else {
        $('#charNum').text("");
        $('#charNum').hide("fast");
    }
};

$( document ).ready(function() {
    $('#charNum').hide();
});