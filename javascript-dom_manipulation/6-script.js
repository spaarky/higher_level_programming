const characterElement = document.getElementById('character');
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to fetch character data');
    }
  })
  .then((data) => {
    const characterName = data.name;
    characterElement.textContent = characterName;
  })
  .catch((error) => {
    console.error('Error:', error);
  });
