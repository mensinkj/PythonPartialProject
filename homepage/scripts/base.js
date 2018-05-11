$(function() {


	$('#show_login_dialog').on('click', function() {
		
		$.loadmodal({
			url: '/homepage/login.post_form/',
			title: 'Login:',
		});//dictionary

	});//click

});//ready


$(function() {


	$('#search').on('change', function() {
		
		ajax({
			url:'/shopping/index.search/' + $('#search').val() + '/',
			success: function(data) {

				$('#products').html(data);
			},//success
		});//ajax

	});//change

});//ready