<%inherit file="base.mako"/>
<%block name="html_tag"><html class="no-js login" lang="en"> </%block>
<%block name="head">${parent.head()}
    <!-- Include OneID javascript API -->
    <script src="//api.oneid.com/js/oneid.js"></script></%block>

<div id="login_page">
  <!-- Login page -->
  <div id="login">
    <div class="row-fluid fluid">
      <div class="span5"> <img src="img/thumbnail_george2.jpg" /> </div>
      <div class="span7">
        <div class="title">
          <span class="name"></span>
          <span class="subtitle">Locked</span>
        </div>
          <div id="oneid-signin-button"></div>
        <!--<form class="form-search row-fluid ">
          <div class="input-append row-fluid fluid">
            <input type="text" class="row-fluid search-query" placeholder="Password">
            <a href="index.html" class="btn color_4">Go</a> </div>
        </form>-->
      </div>
    </div>
  </div>
  <!-- End #login -->
  <!-- <img src="img/ajax-loader.gif"> -->
</div>
<!-- End #loading -->

<%block name="javascript">
<!-- Le javascript
     ========================================================== -->
<!-- Placed at the end of the document so the pages load faster -->

<!-- Flip effect on login screen -->
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
<script type="text/javascript" src="js/plugins/jquerypp.custom.js"></script>
<script type="text/javascript" src="js/plugins/jquery.bookblock.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.uniform.min.js"></script>
<script type="text/javascript">
      $(function() {
        var Page = (function() {

          var config = {
              $bookBlock: $( '#bb-bookblock' ),
              $navNext  : $( '#bb-nav-next' ),
              $navPrev  : $( '#bb-nav-prev' ),
              $navJump  : $( '#bb-nav-jump' ),
              bb        : $( '#bb-bookblock' ).bookblock( {
                speed       : 800,
                shadowSides : 0.8,
                shadowFlip  : 0.7
              } )
            },
            init = function() {

              initEvents();

            },
            initEvents = function() {

              var $slides = config.$bookBlock.children(),
                  totalSlides = $slides.length;

              // add navigation events
              config.$navNext.on( 'click', function() {
              $("#arrow_register").fadeOut();
              $(".not-member").slideUp();
              $(".already-member").slideDown();
                config.bb.next();
                return false;

              } );

              config.$navPrev.on( 'click', function() {

                 $(".not-member").slideDown();
                $(".already-member").slideUp();
                config.bb.prev();
                return false;

              } );

              config.$navJump.on( 'click', function() {

                config.bb.jump( totalSlides );
                return false;

              } );

              // add swipe events
              $slides.on( {

                'swipeleft'   : function( event ) {

                  config.bb.next();
                  return false;

                },
                'swiperight'  : function( event ) {

                  config.bb.prev();
                  return false;

                }

              } );

            };

            return { init : init };

        })();

        Page.init();

      });
</script>
<script type='text/javascript'>

    $(window).load(function() {
     $('#loading1').fadeOut();
    });
      $(document).ready(function() {
           $("input:checkbox, input:radio, input:file").uniform();


      $('[rel=tooltip]').tooltip();
      $('body').css('display', 'none');
      $('body').fadeIn(500);

      $("#logo a, #sidebar_menu a:not(.accordion-toggle), a.ajx").click(function() {
        event.preventDefault();
        newLocation = this.href;
        $('body').fadeOut(500, newpage);
        });
        function newpage() {
        window.location = newLocation;
        }
      });
</script>
<script type="text/javascript">
    OneID.init({
     buttons: {
       "signin #oneid-signin-button": [{
         challenge: {
           "request_method": "POST",
           "callback": "/dashboard",
           "attr": "email name"
         }
       }]
     }
    });
</script>
</%block>

