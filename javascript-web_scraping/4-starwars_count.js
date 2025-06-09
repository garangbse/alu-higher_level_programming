#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.filter(film =>
    film.characters.some(character => character.includes('/18/'))
  ).length;

  console.log(count);
});
