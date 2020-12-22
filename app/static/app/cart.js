$(function () {
    let cart;

    function clearCart() {
        cart = {
            items: {},
            restaurant: null,
            total: 0.0
        }
        saveCart()
    }

    function saveCart() {
        updateTotal()
        localStorage.setItem('cart', JSON.stringify(cart))
    }

    // init cart
    if (localStorage.getItem('cart') === null) {
        clearCart()
    } else {
        cart = JSON.parse(localStorage.getItem('cart'))
        for (let itemId in cart.items) {
            if (cart.items.hasOwnProperty(itemId)) {
                createUIItem(itemId)
            }
        }
        updateTotal()
    }

    function updateTotal() {
        let cartTotal = 0.0
        for (let itemId in cart.items) {
            if (cart.items.hasOwnProperty(itemId)) {
                cartTotal += cart.items[itemId].totalPrice
            }
        }
        cart.total = parseFloat(cartTotal.toFixed(2))
        $('span.total-price').text(cartTotal.toFixed(2))
    }

    function createUIItem(itemId) {
        // This function requires cart variable to be properly updated first
        let cartItemsDiv = $('div#cartModalStep')
        // Init elements
        let cartItem = $('<div/>', {class: 'cart-item'})
        let cartItemInput = $('<input>', {
            type: 'hidden',
            class: 'cart-item-id',
            value: itemId
        })
        let cartItemQty = $('<div/>', {
            class: 'cart-item-qty'
        }).append([
            $('<span/>', {
                class: 'qty',
                text: cart.items[itemId].count
            }),
            $('<span/>', {
                text: 'X'
            })
        ])
        let cartItemNameDiv = $('<div/>', {
            class: 'cart-item-name'
        }).append($('<span/>', {
            class: 'name',
            text: cart.items[itemId].name
        }))
        let cartItemQtyButtons = $('<div/>', {
            class: 'cart-item-qty-buttons'
        }).append(
            $('<div/>', {
                class: 'btn-group'
            }).append([
                $('<button/>', {
                    type: 'button',
                    class: 'btn btn-sm btn-outline-danger plus-qty-btn',
                    html: '<i class="fas fa-plus"></i>'
                }),
                $('<button/>', {
                    type: 'button',
                    class: 'btn btn-sm btn-outline-danger minus-qty-btn',
                    html: '<i class="fas fa-minus"></i>'
                })
            ])
        )
        let cartItemPrice = $('<div/>', {
            class: 'cart-item-price'
        }).append([
            $('<span/>', {
                class: 'price',
                text: cart.items[itemId].totalPrice
            }),
            $('<span/>', {
                class: 'currency',
                text: cart.items[itemId].currency
            })
        ])
        let itemDelButton = $('<div/>', {
            class: 'cart-item-del-button'
        }).append($('<button/>', {
            type: 'button',
            class: 'btn btn-sm btn-outline-danger del-item-btn',
            html: '<i class="far fa-trash-alt"></i>'
        }))

        // Construct cartItem
        cartItem.append([
            cartItemInput,
            cartItemQty,
            cartItemNameDiv,
            cartItemQtyButtons,
            cartItemPrice,
            itemDelButton
        ])
        // Add cart item to item list
        cartItemsDiv.prepend(cartItem)
        // Add alert or popup notification that the item has been added
    }

    function increaseItemQty(itemId) {
        // Update JS object
        cart.items[itemId].count += 1
        cart.items[itemId].totalPrice += cart.items[itemId].basePrice
        cart.items[itemId].totalPrice = parseFloat(cart.items[itemId].totalPrice.toFixed(2))
        // Update UI
        let cartItemDiv = $('div.cart-item :input[class="cart-item-id"]').filter(function () {
            return this.value === itemId
        }).parents('div.cart-item')[0]
        $(cartItemDiv).find('.cart-item-price > span.price').text(cart.items[itemId].totalPrice.toFixed(2))
        $(cartItemDiv).find('.cart-item-qty > span.qty').text(cart.items[itemId].count)
        saveCart()
    }

    function decreaseItemQty(itemId) {
        if (cart.items[itemId].count > 1) {
            // Update JS object
            cart.items[itemId].count -= 1
            cart.items[itemId].totalPrice -= cart.items[itemId].basePrice
            cart.items[itemId].totalPrice = parseFloat(cart.items[itemId].totalPrice.toFixed(2))
            // Update UI
            var cartItemDiv = $('div.cart-item :input[class="cart-item-id"]').filter(function () {
                return this.value === itemId
            }).parents('div.cart-item')[0]
            $(cartItemDiv).find('.cart-item-price > span.price').text(cart.items[itemId].totalPrice.toFixed(2))
            $(cartItemDiv).find('.cart-item-qty > span.qty').text(cart.items[itemId].count)
            saveCart()
        }
    }

    function addItem(target) {
        let itemDiv = $(target).parents('div.menu-item')[0]
        let itemId = itemDiv.id
        let itemName = $(itemDiv).find('.item-name')[0].textContent
        let itemPrice = parseFloat($(itemDiv).find('.item-price')[0].textContent)
        let itemCurrency = $(itemDiv).find('.item-currency')[0].textContent
        if (cart.items.hasOwnProperty(itemId)) {
            increaseItemQty(itemId)
        } else {
            cart.items[itemId] = {
                'name': itemName,
                'basePrice': itemPrice,
                'totalPrice': itemPrice,
                'currency': itemCurrency,
                'count': 1
            }
            createUIItem(itemId)
            saveCart()
        }
    }

    function deleteItem(itemId) {
        delete cart.items[itemId]
        let cartItemDiv = $('div.cart-item :input[class="cart-item-id"]').filter(function () {
            return this.value === itemId
        }).parents('div.cart-item')[0]
        cartItemDiv.remove()
        saveCart()
    }

    // Restaurant Menu add button
    $('.add-item').click(function (e) {
        addItem(e.target)
    })

    // Cart buttons
    $('div#cartModalStep').on('click', '.plus-qty-btn', function (e) {
        let itemId = $(e.target).parents('div.cart-item').find('input.cart-item-id').val()
        increaseItemQty(itemId)
    })

    $('div#cartModalStep').on('click', '.minus-qty-btn', function (e) {
        let itemId = $(e.target).parents('div.cart-item').find('input.cart-item-id').val()
        decreaseItemQty(itemId)
    })

    $('div#cartModalStep').on('click', '.del-item-btn', function (e) {
        let itemId = $(e.target).parents('div.cart-item').find('input.cart-item-id').val()
        deleteItem(itemId)
    })
})
