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
  $('#btnEndStep2').click(function () {
    $('#step2').addClass('hideMe')
    $('#step3').removeClass('hideMe')
  })
  $('#btnEndStep3').click(function () {
    // Whatever your final validation and form submission requires
    $('#sampleModal').modal('hide')
  })
})
