$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  let movies = data.result;
  let ul = $('#list_movies');

  $.each(movies, function(index, movie) {
    let li = $('<li>').text(movie.title);
    ul.append(li);
  });
});
