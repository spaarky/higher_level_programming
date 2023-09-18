$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        let translation = data.hello;
        $('#hello').text(translation);
    });
});
