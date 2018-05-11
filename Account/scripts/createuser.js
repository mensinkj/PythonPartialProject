$(function() {

	$('#id_username').on('change',function() {

		var username = $('#id_username').val();
		$.ajax({
			url: '/Account/index.check_username/',
			type:"POST",
			data: {
				'u': username,
			},//data
			success: function(resp) {
				if (resp == 'pass') { //unused username (good)
					$('#id_username_message').text("This Username is Approved.");
				}else{ //already used (bad)
					$('#id_username_message').text("This Username is already used.");

				}//if
			},//success
		});s//ajax
	});//change

});//ready