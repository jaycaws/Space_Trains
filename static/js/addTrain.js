$(function(){
	$('#buttonRegisterTrain').click(function(){

		$.ajax({
			url: '/addTrain',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});