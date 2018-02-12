var page_url = "127.0.0.1:8000";
(function($) {

	"use strict";

//   	/*---------------------------------------------------- */
//    /* ajaxchimp
// 	------------------------------------------------------ */

	// Example MailChimp url: http://xxx.xxx.list-manage.com/subscribe/post?u=xxx&id=xxx
	var sLoader = $('#submit2-loader');
	sLoader.fadeOut();
	$("#submit").on('click',(e)=>{
		e.preventDefault();
		$('#message2-warning').html(`Sending...`);
		$('#message2-warning').fadeIn();
		var product = {id:  e.currentTarget.id}
					
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var name = document.getElementById("name").value;
		var message = document.getElementById("text").value;
		var phone = document.getElementById("phone").value;
		var url = `http://${page_url}/sendmail`;
		var sLoader = $('#submit2-loader');
		sLoader.fadeIn(); 
		$.ajax({
			type: "POST",
			url,
			data: { csrfmiddlewaretoken: token,   // < here 
					state:"inactive" , 
					name: name,
					message: message,
					phone:phone,
					//file,
				  },
				  async: true,
			success: function(res) {
				sLoader.fadeOut(); 
				$('#message2-warning').html(JSON.parse(res));
				$('#message2-warning').fadeIn(4000);
			},
			error: function(){
				$('#message2-warning').html(`Something went wrong. Please try again.`);
				$('#message2-warning').fadeIn(45000);
				sLoader.fadeOut();
			}
		})
	}) 
	
		      	

	/*---------------------------------------------------- */
	/*	contact form
	------------------------------------------------------ */
})(jQuery);