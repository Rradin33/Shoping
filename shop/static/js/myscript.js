//  in ajax marbot b ( def status_of_shop_cart ) daron views.py ast, baraye in ast k vaghti roye kalaha click mikonim k k b sabade kharid ezafe beshan roye ax sabade kharid yek adad kochik neshan dade beshe k chandta kala daron sabade kharid hast 

function status_of_shop_cart() {
	$.ajax({
		type:"GET",
		url:"/orders/status_of_shop_cart/",
		success: function(res) {
			$("#indicator__value").text(res);
		}
	});
}
status_of_shop_cart()


// ----------------------------------------------------------------

// in ajax pain merbod b ( def add_to_shop_cart ) daron view.py ast, yani marbot b add kardan yek kala b sabade kharid ast

function add_to_shop_cart(product_id, qty) {
	if(qty===0) {
		qty = $("#product_quantity").val();
		alert(qty);
	}
	$.ajax({
		type:"GET",
		url:"/orders/add_to_shop_cart/",
		data:{
			product_id: product_id,
			qty:qty
		},
		success: function(res) {
		alert(res);
			alert("Kalaye morede nazar b sabad kharid shoma ezafe shod");
			$("#indicator__value").text(res);
			status_of_shop_cart()
		}
	});
}

// ----------------------------------------------------------------

// in ajax pain merbod b ( def delete_from_shop_cart ) daron view.py ast, yani marbot b delete kardan yek kala b sabade kharid ast

function delete_from_shop_cart(prodyct_id) {
	$.ajax({
		type:"GET",
		url:"/orders/delete_from_shop_cart/",
		data:{
			product_id: product_id,
			qty:qty
		},
		success: function(res) {
		alert(res);
			alert("Kalaye morede nazar az sabad kharid shoma hazf shod");
			$("#shop_cart_list").html(res);
			status_of_shop_cart()
		}
	});
}

// ----------------------------------------------------------------

// in code baraye dokme be roz rasani daron safhe sabade kharid ast

function update_shop_cart() {
	var product_id_list = []
	var qty_list = []
	$("input[id^='qty_']").each(function(index){
		product_id_list.push($(this).attr('id').slice(4));
		qty_list.push($(this).val())
	});
	$.ajax({
		type:"GET",
		url:"/orders/update_shop_cart/",
		data:{
			product_id_list: product_id_list,
			qty_list: qty_list
		},
		success: function(res) {
			alert("zkrfnlkn")
			$("#shop_cart_list").html(res);
			status_of_shop_cart()
		}
	});
}

// ----------------------------------------------------------------

// in ajax marbot b ( class CommentView ) ast baraye inke moshtari betavanad comment bedahad

function showCreateCommentForm(productId, commentId, slug) {
	$.ajax({
		type: "GET",
		url: "/csf/create_comment/" + slug,
		data: {
			productId: productId,
			commentId: commentId,
		},
		success: function(res) {
			$("#btn_" + commentId).hide();
			$("#comment_form_" + commentId).html(res);
		}
	});
}

// ----------------------------------------------------------------

// in ajax marbot b ( class favorite ) dakhele models.py ast

function addToFavorites(productId) {
	$.ajax({
		type:"GET",
		url:"/csf/add_to_favorite/",
		data:{
			productId: productId,
		},
		success: function(res) {
			alert("res");
		}
	});
}

