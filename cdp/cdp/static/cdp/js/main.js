$(document).ready(function(){

	var checks = $('.fields .field input[type="checkbox"]');
	checks.click(function(){
		var checked = $(this).is(':checked');
		var id = $(this).attr('id');
		$(this)[checked? 'addClass': 'removeClass']('checked');

		$('#label_' + id)[checked? 'addClass': 'removeClass']('checked')
	})
})