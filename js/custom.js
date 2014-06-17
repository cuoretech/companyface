    $("#menu-close").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
    });

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
    });

    $(function () {
      $(".youtube").YouTubeModal({autoplay:0, width:640, height:360});
    });

    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });

$(window).load(function() {
  'use strict';
  //preloader
  $(window).scrollTop(0);
  $('#status').fadeOut();
  $('#preloader').delay(350).fadeOut('slow');

  //if link points to nowhere (aka #) then don't go to top of page
  $('a[href="#"]').click(function() {
    return false;
  });

});

$(document).ready(function() {
  'use strict';

  $('.navbar a, .navbar li a, .brand, #footer li a, .more a, a.go-top')
  .bind('click', function(event) {
    var $anchor = $(this),
    scrollVal = $($anchor.attr('href')).offset().top - 60;

    if (scrollVal < 0) {
      scrollVal = 0;
    }

    $('[data-spy="scroll"]').each(function() {
      $(this).scrollspy('refresh');
    });

    $.scrollTo(scrollVal, {
      easing: 'easeInOutExpo',
      duration: 1500
    });

    event.preventDefault();
  });

  //sharre
  $('.social .holder').sharrre({
    share: {
      googlePlus: true,
      facebook: true,
      twitter: true
    },
    buttons: {
      twitter: {
        custom: 'Cuore - http://www.cuore.io/ Sync Your World',
        via: 'Cuore',
        url: false
            }
    },
    template: '<div class="container"><div class="soc-item google"><a href=""><span class="name">Google +</span><span class="count">1,600</span></a></div>' +
                '<div class="soc-item-holder"><div class="soc-item twitter"><a href=""><span class="name">Twitter</span> <span class="count">1,600</span></a></div>' +
                '<div class="soc-item facebook"><a href=""><span class="name">Facebook</span> <span class="count">1,600</span></a></div></div></div>',
    urlCurl: 'http://dribbbleboard.com/js/sharrre.php',
    enableHover: false,
    className: '',
    render: function(api, options) {
      $(api.element).on('click', '.twitter', function() {
        api.openPopup('twitter');
      });
      $(api.element).on('click', '.facebook', function() {
        api.openPopup('facebook');
      });
      $(api.element).on('click', '.google', function() {
        api.openPopup('googlePlus');
      });
      $('.social .google .count').text(options.count.googlePlus);
      $('.social .twitter .count').text(options.count.twitter);
      $('.social .facebook .count').text(options.count.facebook);
      var summ = options.count.googlePlus + options.count.twitter + options.count.facebook;
      console.log("Shares summary: "+summ);
        }
    });

  //animated elements
  if ($('.no-touch').length) {
    skrollr.init({
      edgeStrategy: 'set',
      easing: {
        WTF: Math.random,
        inverted: function(p) {
          return 1 - p;
        }
      },
      smoothScrolling: true,
      forceHeight: false
    });
  }
});