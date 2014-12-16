// #menu-overlay
$("#login").click(function () {
          $(".menu-overlay").slideDown(750);
       });

$(".login-close").click(function () {
          $(".menu-overlay").fadeOut(750);
       });


$(".signup-close").click(function () {
          $(".signup-overlay").fadeOut(750);
       });

$("#signup").click(function () {
          $(".signup-overlay").slideDown(750);
       });
