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
                console.log('Not Logged in')
            }else{
                updateUserOrder(menuitemId, action)
            }
    })       
}}

function updateUserOrder(menuitemId, action){
    console.log('User is logged in, sending data...')

    var url = '/update_item/'

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
    })
}