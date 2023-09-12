const movieList = document.getElementById('list_movies');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to fetch movie data');
    }
  })
  .then((data) => {
    const movies = data.results;

    movies.forEach((movie) => {
      const title = movie.title;
      const listItem = document.createElement('li');
      listItem.textContent = title;
      movieList.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
    movieList.textContent = 'Error: Failed to fetch movie data';
  });
