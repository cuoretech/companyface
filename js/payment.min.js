		    // This identifies your website in the createToken call below
		    Stripe.setPublishableKey('pk_test_aMLfjYjMU7J233NCdfwFUMTf');
		 
		    var stripeResponseHandler = function(status, response) {
		      var $form = $('#payment-form');
		 
		      if (response.error) {
		        // Show the errors on the form
		        $form.find('.payment-errors').text(response.error.message);
		        $form.find('button').prop('disabled', false);
		      } else {
		        // token contains id, last4, and card type
		        var token = response.id;
		        // Insert the token into the form so it gets submitted to the server
		        $form.append($('<input type="hidden" name="stripeToken" />').val(token));
		        // and re-submit
		        $form.get(0).submit();
		      }
		    };
		 
		    jQuery(function($) {
		      $('#payment-form').submit(function(e) {
		        var $form = $(this);
		 
		        // Disable the submit button to prevent repeated clicks
		        $form.find('button').prop('disabled', true);
		 
		        Stripe.card.createToken($form, stripeResponseHandler);
		 
		        // Prevent the form from submitting with the default action
		        return false;
		      });
		    });

		    $(function($){
		      $('[data-numeric]').payment('restrictNumeric');
		      $('.cc-number').payment('formatCardNumber');
		      $('.cc-exp').payment('formatCardExpiry');
		      $('.cc-cvc').payment('formatCardCVC');

		      $('form.pay').submit(function(e){
		        e.preventDefault();
		        $('input').removeClass('invalid');
		        $('.validation').removeClass('passed failed');

		        var cardType = $.payment.cardType($('.cc-number').val());

		        $('.cc-number').toggleClass('invalid', !$.payment.validateCardNumber($('.cc-number').val()));
		        $('.cc-exp').toggleClass('invalid', !$.payment.validateCardExpiry($('.cc-exp').payment('cardExpiryVal')));
		        $('.cc-cvc').toggleClass('invalid', !$.payment.validateCardCVC($('.cc-cvc').val(), cardType));

		        if ( $('input.invalid').length ) {
		          $('.validation').addClass('failed');
		        } else {
		          $('.validation').addClass('passed');
		        }
		      });
		  	});