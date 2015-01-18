// #menu-overlay
$("#login").click(function () {
          $(".menu-overlay").slideDown(750);
          $( "body" ).addClass( "noscroll" );
       });

$(".login-close").click(function () {
          $(".menu-overlay").fadeOut(750);
          $( "body" ).removeClass( "noscroll" )
       });


$(".signup-close").click(function () {
          $(".signup-overlay").fadeOut(750);
          $( "body" ).removeClass( "noscroll" )
       });

$(".signup").click(function () {
          $(".signup-overlay").slideDown(750);
          $( "body" ).addClass( "noscroll" );
       });

$(".forgotpassword").click(function () {
    $(".forgotpassword-overlay").slideDown(750);
    $( "body" ).addClass( "noscroll" );
});

$(".forgotpassword-close").click(function () {
    $(".forgotpassword-overlay").fadeOut(750);
    $(".menu-overlay").fadeOut(750);
    $( "body" ).removeClass( "noscroll" );
});

//mobile nav

$(".close-mobile-nav").click(function () {
    $(".mobile-nav").slideUp(750);
});