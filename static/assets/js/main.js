/** 
 * ===================================================================
 * Main js
 *
 * ------------------------------------------------------------------- 
 */ 
var page_url = "127.0.0.1:8000";
(function($) {

	"use strict";

//   	/*---------------------------------------------------- */
//    /* ajaxchimp
// 	------------------------------------------------------ */

	// Example MailChimp url: http://xxx.xxx.list-manage.com/subscribe/post?u=xxx&id=xxx
	var sLoader = $('#submit2-loader');
	sLoader.fadeOut();
	$("form[name  = 'snob']").on('submit',(e)=>{
		e.preventDefault();
		console.log(e.currentTarget.id)
		var product = {id:  e.currentTarget.id}
					
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var url = `http://${page_url}/cpanel/delete_product/${product.id}/`;
		var sLoader = $('#submit2-loader');
		sLoader.fadeIn(); 
		
		$.ajax({
			type: "POST",
			url,
			data: { csrfmiddlewaretoken: token,   // < here 
					state:"inactive" , 
					product: product.id,
					//file,
				  },
				  async: false,
			success: function() {
				sLoader.fadeOut(); 
				console.log("success")
				$('#message2-warning').html("Successful, You will get an email from us soon");
				$('#message2-warning').fadeIn();
				window.location.replace(`http://${page_url}/cpanel/tables`)
			},
			error: function(){
				console.log("fail")
				$('#message2-warning').html("Something went wrong. Please try again.");
				$('#message2-warning').fadeIn();
				sLoader.fadeOut();
			}
		})
	}) 

	var sLoader = $('#submit2-loader');
	sLoader.fadeOut();
	$("#submit").on('click',(e)=>{
		e.preventDefault();
		$('#message-warning').html(`Signing in...`);
		$('#message-warning').fadeIn();
		
					
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var username = document.getElementById("username").value;
		var password = document.getElementById("password").value;
		var url = `http://${page_url}/cpanel/signin`;
		var sLoader = $('#submit2-loader');
		sLoader.fadeIn(); 
		$.ajax({
			type: "POST",
			url,
			data: { csrfmiddlewaretoken: token,   // < here 
					state:"inactive" , 
					username: username,
					password: password,
					//file,
				  },
				  async: true,
			success: function(res) {
				sLoader.fadeOut(); 
				$('#message-warning').html(JSON.parse(res));
				$('#message-warning').fadeIn(4000);
				if (JSON.parse(res) == "true"){
					window.location.replace(`http://${page_url}/cpanel`)
				}
			},
			error: function(){
				$('#message-warning').html(`Something went wrong. Please try again.`);
				$('#message-warning').fadeIn(45000);
				sLoader.fadeOut();
			}
		})
	}) 
	
	
	sLoader.fadeOut();
	$("#email_submit").on('click',(e)=>{
		e.preventDefault();
		$('#message2-warning').html(`Sending...`);
		$('#message2-warning').fadeIn();
		
					
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var email = document.getElementById("email").value;
		console.dir(email)
		var url = `http://${page_url}/cpanel/set_mail`;
		var sLoader = $('#submit2-loader');
		sLoader.fadeIn(); 
		$.ajax({
			type: "POST",
			url,
			data: { csrfmiddlewaretoken: token,   // < here 
					state:"inactive" , 
					email,
					//file,
				  },
				  async: false,
			success: function(res) {
				console.log(res)
				sLoader.fadeOut(); 
				$('#message2-warning').html("something went wrong");
				$('#message2-warning').fadeIn(4000);
				if (res != "error") {
					window.location.reload()
				}
			},
			error: function(){
				$('#message2-warning').html(`Something went wrong. Please try again.`);
				$('#message2-warning').fadeIn(45000);
				sLoader.fadeOut();
			}
		})
	})
			 
	$("#pass_submit").on('click',(e)=>{
		e.preventDefault();
					
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var old = document.getElementById("old").value;
		var newpass = document.getElementById("new").value;
		var retype = document.getElementById("retype").value;
		console.log(old)
		if (old.length < 5  || newpass !== retype || newpass.length < 5) {
			$('#message3-warning').html(`Passwords do not match, ensure to enter atleast 5 characters`);
			$('#message3-warning').fadeIn();
			return 	
		}
		var url = `http://${page_url}/cpanel/set_pass`;
		var sLoader = $('#submit3-loader');
		sLoader.fadeIn(); 
		$.ajax({
			type: "POST",
			url,
			data: { csrfmiddlewaretoken: token,   // < here 
					state:"inactive" , 
					old,
					newpass,
					//file,
				  },
				  async: false,
			success: function(res) {
				console.log(res)
				sLoader.fadeOut(); 
				$('#message3-warning').html(res);
				$('#message3-warning').fadeIn(4000);
				if (res != "error") {
					//window.location.reload()
				}
			},
			error: function(){
				$('#message3-warning').html(`Something went wrong. Please try again.`);
				$('#message3-warning').fadeIn(45000);
				sLoader.fadeOut();
			}
		})
	})

	/*---------------------------------------------------- */
	/*	contact form
	------------------------------------------------------ */
})(jQuery);