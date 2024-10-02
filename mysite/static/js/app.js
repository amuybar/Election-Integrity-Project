// JS FILE FOR OPENNING AND CLOSING THE MENU
$(document).ready(function() {
    // console.log("Entered Javascript");
    $('#menu-icon').click(function() {
        $('#nav-links').toggleClass('active');
        $('#menu-icon').toggleClass('active');
    // Disable scrolling when menu is open
    $("body").toggleClass("no-scroll");
    });
});

