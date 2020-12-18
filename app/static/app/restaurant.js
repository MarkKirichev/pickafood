function createOrder() {
    let date = $('#datePicker').val()
    let time = $('#timePicker').val()
    let peopleNumber = $('#peopleNumber').val()
    let names = $('#names').val()
    let phoneInput = $('#phoneInput').val()
    let emailInput = $('#emailInput').val()

    let cart = JSON.parse(localStorage.getItem('cart'))
    let data = {
        date,
        time,
        peopleNumber,
        names,
        phoneInput,
        emailInput,
        cart
    }

    const headers = {
        'content-type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken'),
    };

    $.ajax({
        url: '/order',
        type: 'post',
        data: JSON.stringify(data),
        headers: headers,
        success: function () {
            // Show a success modal. Clear cart and input fields
            alert('We did it bro!')
        }
    });

}

$(function () {
    let $datePicker = $('#datePicker')
    $datePicker.click(function () {
        $datePicker.pickadate({
            containerHidden: 'body',
            container: 'body',
            format: 'dd/mm/yyyy',
            min: Date.now()
        })
    })
    let $timePicker = $('#timePicker')
    $timePicker.click(function () {
        $timePicker.pickatime({
            containerHidden: 'body',
            container: 'body',
            format: 'HH:i'
        })
    })

    // Booking modals
    $('#toBookingInfo').click(function () {
        $('#cartModalStep').addClass('hidden-modal-body')
        $('#bookingModalStep').removeClass('hidden-modal-body')
    })
    $('#confirmReservation').click(function () {
        createOrder()
    })

    $('#btnEndStep2').click(function () {
        $('#step2').addClass('hideMe')
        $('#step3').removeClass('hideMe')
    })
    $('#btnEndStep3').click(function () {
        // Whatever your final validation and form submission requires
        $('#sampleModal').modal('hide')
    })
})
