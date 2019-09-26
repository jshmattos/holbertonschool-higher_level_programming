$(document).ready(() => {
  $('#btn_translate').click(() => {
    const val = $('#language_code').val()
    $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${val}`, data => {
      $('#hello').append(`<p>${data.hello}</p>`)
    })
  })
  $('#language_code').on('keypress', e => {
    if (e.which === 13) {
      const val = $('#language_code').val()
      $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${val}`, data => {
        $('#hello').append(`<p>${data.hello}</p>`)
      })
    }
  })
})
