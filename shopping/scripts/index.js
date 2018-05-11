$(function() {
	$('.add_button').on('click', function(evt) {
		
		var pid = $(this).attr('data-pid');
		var qty = $(this).closest('.item_container').find('.qty').val();

		$.loadmodal({
			url: "/shopping/shopping_cart.additem/" + pid + "/" + qty,
			title: 'Shopping Cart',
			width: '700px',
		});//load modal
	});//click
});//ready