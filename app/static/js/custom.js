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
$('.editCategoryBtn').click(function(){
	$('#editCategoryModal').modal('show');
	$('#editCategoryModal #editRecipeCategoryTitle').text('Edit '+$(this).data('name'))
	$('#editCategoryModal #editRecipeCategoryInput').val($(this).data('name'));
	$('#editCategoryModal #editRecipeCategoryForm').attr('action',$(this).data('action'));
});
$('.deleteCategoryBtn').click(function(){
	$('#deleteCategoryModal').modal('show');
	$('#deleteCategoryLink').attr('href',$(this).data('action'));
});
$('.editRecipeBtn').click(function(){
	$('#editRecipeModal').modal('show');
	$('#editRecipeModal #editRecipeForm #recipeName').val($(this).data('name'))
	$('#editRecipeModal #editRecipeForm #recipeDescription').val($(this).data('description'));
	$('#editRecipeModal #editRecipeForm').attr('action',$(this).data('action'));
});
$('.deleteRecipeBtn').click(function(){
	$('#deleteRecipeModal').modal('show');
	$('#deleteRecipeLink').attr('href',$(this).data('action'));
});

