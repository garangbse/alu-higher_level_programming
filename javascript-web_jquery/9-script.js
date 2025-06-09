$(document).ready(function() {
    $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            $('#hello').text(response.hello);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching hello:', error);
            $('#hello').text('Error loading translation');
        }
    });
});
