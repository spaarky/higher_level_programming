function fetchHello () {
    const helloElement = document.getElementById('hello');
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        const helloTranslation = data.hello;
        helloElement.textContent = helloTranslation;
      })
      .catch((error) => {
        console.error('Fetch error:', error);
      });
  }

  document.addEventListener('DOMContentLoaded', fetchHello);
