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
    // Take all reservation fields and construct a json object
    // send a POST request via $ AJAX to an endpoint for ex. /reservations
    // the POST /reservations endpoint should validate the json input (this is extra)
    // then the data should be stored to the database (opravqi sa moi, pravi si modeli ako trqbwa)
    // Disable the default sumbit function of the button aka make it not a submit button
    // Create a new modal called successfulReservation showing a success message
    // have fun!
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
