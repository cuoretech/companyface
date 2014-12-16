

$(document).ready(function () {

    "use strict";

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    // text change on click in portfolio
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
        $(".filterAll").click(function(){
            $(".activeFilter h3 span").text(function(){
                return 'all';
            });
        });


        $(".filterGraphics").click(function(){
            $(".activeFilter h3 span").text(function(){
                return 'graphics';
            });
        });

        $(".filterVideo").click(function(){
            $(".activeFilter h3 span").text(function(){
                return 'video';
            });
        });

        $(".filterMix").click(function(){
            $(".activeFilter h3 span").text(function(){
                return 'mix';
            });
        });


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    //process section navigation
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    (function() {

        [].slice.call( document.querySelectorAll( '.tabs' ) ).forEach( function( el ) {
            new CBPFWTabs( el );
        });

    })();



    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* Intro Height  */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

    function introHeight() {
        var wh = $(window).height();
        $('#intro').css({height: wh});
    }

    introHeight();
    $(window).bind('resize',function () {
        //Update slider height on resize
        introHeight();
    });


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* contact form init  */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

    $('#contactform').submit(function(){
        var action = $(this).attr('action');
        $("#result").slideUp(300,function() {
            $('#result').hide();
            $('#submit')
                .attr('disabled','disabled');
            $.post(action, {
                    name: $('#name').val(),
                    email: $('#email').val(),
                    phone: $('#phone').val(),
                    comments: $('#comments').val(),
                },
                function(data){
                    document.getElementById('result').innerHTML = data;
                    $('#result').slideDown('slow');
                    $('#submit').removeAttr('disabled');
                    if(data.match('success') != null) $('#contactform').slideUp('slow');
                }
            );

        });

        return false;

    });


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* click switched with touch for mobile  */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/


    $('.gallery-inner img').bind('touchstart', function() {
        $(this).addClass('.gallery-inner  .captionWrapper');
    });

    $('.gallery-inner  img').bind('touchend', function() {
        $(this).removeClass('.gallery-inner  .captionWrapper');
    });


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* Parallax init  */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/




    if(jQuery.browser.mobile)
    {

        /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
        //hide the parallax letters on mobile devices
        /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
        $(function() {
            $('.parallaxLetter').css({
                display: 'none'
            });
        });


        //stop timers from counting
        $('.timer1').countTo({

            from: 0, // the number you want to start
            to: 8679, // the number you want to reach
            speed: 1,
            refreshInterval: 8679

        });

        // second timer
        $('.timer2').countTo({

            from: 0,// the number you want to start
            to: 340,// the number you want to reach
            speed: 1,
            refreshInterval: 340

        });


        // third timer
        $('.timer3').countTo({

            from: 0,// the number you want to start
            to: 100,// the number you want to reach
            speed: 1,
            refreshInterval: 100
        });


        // fourth timer
        $('.timer4').countTo({

            from: 0,// the number you want to start
            to: 3456,// the number you want to reach
            speed: 1,
            refreshInterval: 3456


        });

    }
    else
    {


        // init scrollreveal plugin
        window.scrollReveal = new scrollReveal();

        // launch timers on reveal only on desktops and laptops
        $('#text-separator-timers').waypoint(function() {
            "use strict";
            // first timer
            $('.timer1').countTo({

                from: 0, // the number you want to start
                to: 8679, // the number you want to reach
                speed: 4000,
                refreshInterval: 100

            });

            // second timer
            $('.timer2').countTo({

                from: 0,// the number you want to start
                to: 340,// the number you want to reach
                speed: 2500,
                refreshInterval: 50

            });


            // third timer
            $('.timer3').countTo({

                from: 0,// the number you want to start
                to: 100,// the number you want to reach
                speed: 2000,
                refreshInterval: 10
            });


            // fourth timer
            $('.timer4').countTo({

                from: 0,// the number you want to start
                to: 3456,// the number you want to reach
                speed: 4000,
                refreshInterval: 10,


            });


        }, { offset: 500 });



    }


    //parallax initialised only on desktops and laptops
    if(!(jQuery.browser.mobile) && $(window).width() > 768){
        $(window).stellar({
            responsive: true,
            horizontalOffset: 0,
            horizontalScrolling:false
        });
    }

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* fitvids */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    $('body').fitVids();


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* Isotope */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    var $container = $('.gallery').imagesLoaded( function() {
        $container.isotope({
            // options
        });
    });


    $('#filters').on( 'click', 'button', function() {
        var filterValue = $(this).attr('data-filter');
        $container.isotope({ filter: filterValue });
    });

    $container.isotope({
        filter: '*' // IF YOU WANT TO DISPLAY AT FIRST ONLY ONE FILTER, FOR EXAMPLE DESIGNS: SUBSTIUTE '*' WITH '.designs'
    });




    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* overlay portfolio */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    $("a.overlay-ajax").click(function(){
        var url = $(this).attr("href");

        $(".overlay-section").load(url + ' #transmitter');
        $('.overlay-close img').tooltip();
        return false;
    });

    $(".overlay-close").click(function(){
        $(".overlay-section").empty();
    });



    //  no scroll on body when overlay is up
    $(function () {

        $('a.overlay-ajax').click(function(){
            $( "body" ).addClass( "noscroll" );
        });

        $('a.overlay-close').click(function(){
            $( "body" ).removeClass( "noscroll" );
        });
    });


    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* smoothscroll */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    smoothScroll.init({
        speed: 1000,
        offset: 60
    });




    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* owl-carousels */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    $("#owl-team").owlCarousel({
        singleItem:	true,
        autoPlay:	true,
        navigation: true,
        navigationText: [
            "<i class='fa fa-angle-left fa-3x'></i>",
            "<i class='fa fa-angle-right fa-3x'></i>"
        ]
    });



    $("#owl-clients").owlCarousel({
        items:3,
        itemsDesktop : [1199,3],
        itemsDesktopSmall : [980,2],
        itemsTablet: [768,2],
        itemsMobile : [479,1],
        navigation: true,
        navigationText: [
            "<i class='fa fa-angle-left fa-4x'></i>",
            "<i class='fa fa-angle-right fa-4x'></i>"
        ]
    });


    $("#owl-testimonials").owlCarousel({
        singleItem:	true,
        autoPlay:	true
    });


    $("#owl-featured").owlCarousel({
        items:3,
        itemsDesktop : [1199,3],
        itemsDesktopSmall : [980,2],
        itemsTablet: [768,2],
        itemsMobile : [479,1],
        navigation: true,
        navigationText: [
            "<i class='fa fa-angle-left fa-2x featuredNav'></i>",
            "<i class='fa fa-angle-right fa-2x featuredNav'></i>"
        ]
    });



    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* twitter init */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    $('.tweet').twittie({
        username: 'artbreeze02',
        list: 'envato-tf',
        count: 2
    });

});

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    /* stepform */
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
$(function() {

//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            //as the opacity of current_fs reduces to 0 - stored in "now"
            //1. scale current_fs down to 80%
            scale = 1 - (1 - now) * 0.2;
            //2. bring next_fs from the right(50%)
            left = (now * 50)+"%";
            //3. increase opacity of next_fs to 1 as it moves in
            opacity = 1 - now;
            current_fs.css({'transform': 'scale('+scale+')'});
            next_fs.css({'left': left, 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        }, 
        //this comes from the custom easing plugin
        easing: 'easeInOutBack'
    });
});

$(".previous").click(function(){
    if(animating) return false;
    animating = true;
    
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();
    
    //de-activate current step on progressbar
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    
    //show the previous fieldset
    previous_fs.show(); 
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
            //as the opacity of current_fs reduces to 0 - stored in "now"
            //1. scale previous_fs from 80% to 100%
            scale = 0.8 + (1 - now) * 0.2;
            //2. take current_fs to the right(50%) - from 0%
            left = ((1-now) * 50)+"%";
            //3. increase opacity of previous_fs to 1 as it moves in
            opacity = 1 - now;
            current_fs.css({'left': left});
            previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
        }, 
        duration: 800, 
        complete: function(){
            current_fs.hide();
            animating = false;
        }, 
        //this comes from the custom easing plugin
        easing: 'easeInOutBack'
    });
});

$(".submit").click(function(){
    return false;
})

});

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-36251023-1']);
  _gaq.push(['_setDomainName', 'jqueryscript.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

/*end step form*/