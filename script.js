// to support brython


$(function() {

$('#start').click(function(){
	$('#next').addClass('active');
	$('.selected').removeClass('selected');
	console.log('works?');
});

$('#next').click(function(){
	$('.selected').removeClass('selected');
//	$('.{select}').removeClass('{select}')
	$('.pc_item').addClass('{select}')
});




$('.select').click(function(){
	$(this).addClass('selected');
	console.log('works?');
});


});





