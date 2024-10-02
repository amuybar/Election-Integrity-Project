// JS FILE FOR OPENNING AND CLOSING THE MENU
$(document).ready(function() {
    $('#menu-icon').click(function() {
        $('#nav-links').toggleClass('active');
        $(this).toggleClass('active');
    });
});
