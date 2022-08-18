$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
       var inc_value= $(this).closest('.service-data').find('.qty-input').val();
       var value =parseInt(inc_value,10) ;
       value = isNaN(value) ? 0 : value ;
       if (value <10) {
        value++;
        $(this).closest('.service-data').find('.qty-input').val(value);
       }
    });
     $('.decrement-btn').click(function (e) {
        e.preventDefault();
       var dec_value= $(this).closest('.service-data').find('.qty-input').val();
       var value =parseInt(dec_value,10) ;
       value = isNaN(value) ? 0 : value ;
       if (value >1) {
        value--;
        $(this).closest('.service-data').find('.qty-input').val(value);
       }
    });
    $('.addToCartBtn').click(function (e) {
        e.preventDefault();
        
        var service_id=$(this).closest('.service-data').find('.prod_id').val();
        var product_qty=$(this).closest('.service-data').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

    
        $.ajax({
        method: "POST",
            url: "/add-to-cart",
            data: {
                'service_id': service_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken:token
            },
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
            }
        });
    });

    $(".addToWishlist").click(function (e) { 
        e.preventDefault();
        var service_id=$(this).closest('.service-data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data:{
                'service_id':service_id,
                csrfmiddlewaretoken:token
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
        
    });



    $('.changeQuantity').click(function (e) {
        e.preventDefault();

        var service_id=$(this).closest('.service-data').find('.prod_id').val();
        var product_qty=$(this).closest('.service-data').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();


        $.ajax({
        method: "POST",
            url: "/update-cart",
            data: {
                'service_id': service_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken:token
            },
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
            }
        });
    });
    $(document).on('click','.delete-cart-item', function (e) {
        e.preventDefault();

        var service_id=$(this).closest('.service-data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "delete-cart-item",
            data:  {
                'service_id': service_id,
                csrfmiddlewaretoken:token
            },
            dataType: "dataType",
            success: function (response) {
                alertify.success(response.status)
                $('.cartdata').load(location.href + ".cartdata");
            }
        });

    
    });
    $(document).on('click','.delete-wishlist-item', function (e) {
        

        e.preventDefault();

        var service_id=$(this).closest('.service-data').find('.prod_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data:  {
                'service_id': service_id,
                csrfmiddlewaretoken:token
            },
            dataType: "dataType",
            success: function (response) {
                alertify.success(response.status)
                $('.wishdata').load(location.href + ".wishdata");
            }
        });
        
    });





});