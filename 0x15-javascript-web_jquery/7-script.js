$.getJSON('https://swapi.co/api/people/5/?format=json', data => {
  $('#character').append(`<p>${data.name}</p>`);
});
