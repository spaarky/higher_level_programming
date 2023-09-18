$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
  let charName = data.name;
  $('#character').text(charName);
});
