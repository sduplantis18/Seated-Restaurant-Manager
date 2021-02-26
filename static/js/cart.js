console.log('Hello World')

window.onload = function() {
    var updateBtns = document.getElementsByClassName('updatecart')
    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function(){
            var menuitemId = this.dataset.menuitem
            var action = this.dataset.action
            console.log('menuitemId:', menuitemId, 'Action:', action)
            console.log('USER', user)
            if(user == 'AnonymousUser'){
                addCookieItem(menuitemId, action)
            }else{
                updateUserOrder(menuitemId, action)
            }
    })       
}}

function addCookieItem(menuitemId, action){
    console.log('Not logged in..')
    if(action == 'add'){
        if(cart[menuitemId] == undefined){
            cart[menuitemId] = {'quantity':1}
            console.log('item added to cart')
            
        }else{
            cart[menuitemId]['quantity'] += 1
            console.log('added to cart')
            
        }
        
    }
    if(action == 'remove'){
        cart[menuitemId]['quantity'] -= 1

        if(cart[menuitemId]['quantity'] <= 0){
            console.log('Remove item from cart')
            delete cart[menuitemId]
        }
        
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(menuitemId, action){
    console.log('User is logged in, sending data...')

    var url = '/customer/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'menuitemId': menuitemId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}

// This function hides the shipping-info div form if the user selects the pickup order method.
$(document).ready(function() {
    $('input').change(function() {
      if ($('input[value="pickup"]').is(':checked')) {
        $('#shipping-info').hide();
        /* set the shippinginfo form data to null for each field if the user selected pickup */
        document.getElementById('section').value = "Section";
        document.getElementById('row').value = "Row";
        document.getElementById('seat').value = "0";
      }
      else {
        $('#shipping-info').show();
      }
    });
  });


// This function will clear the cart cookie when a guest user selects the "Clear Cart" button. (This DOES NOT work for logged in users)
function clearCart() {
    var cart = JSON.parse(getCookie('cart'))
    cart = {}
    console.log('Cart cleared')
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
    }