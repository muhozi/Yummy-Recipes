$('.gr-input').focus(function(){
	$(this).prev('.input-group-btn').addClass('input-group-btn-active');
});
$('.gr-input').blur(function(){
	$(this).prev('.input-group-btn').removeClass('input-group-btn-active');
});
$('.gr-textarea').focus(function(){
	$(this).prev('.input-group-btn').addClass('input-group-btn-active');
});
$('.gr-textarea').blur(function(){
	$(this).prev('.input-group-btn').removeClass('input-group-btn-active');
});
$('.recipes-cat .list-group-item').hover(function(){
	$(this).children('.hover-buttons').show();
},
function(){
	$(this).children('.hover-buttons').hide();	
});


