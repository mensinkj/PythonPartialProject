$(function() {
	$('.add_button').on('click', function(evt) {
		
		var pid = $(this).attr('data-pid');
		var qty = $(this).closest('.item_container').find('.qty').val();

		$.loadmodal({
			url: "/rental/rental_cart.additem/" + pid + "/" + qty,
			title: 'Rental Cart',
			width: '700px',
		});//load modal
	});//click
});//ready