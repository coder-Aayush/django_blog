// remap jQuery to $
(function($){

	/* trigger when page is ready */
	$(document).ready(function (){

		// your functions go here
		$('#email-field').click(function() {
			$(this).addClass("active");
       $(this).attr('placeholder','Email Address...');
			$('#subscribe-button').addClass("show");
		});

	});

})(window.jQuery);