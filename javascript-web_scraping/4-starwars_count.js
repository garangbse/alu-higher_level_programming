#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, function (error, response, body) {
    if (error) {
        console.error(error);
        return;
    }
    
    try {
        const films = JSON.parse(body).results;
        const count = films.filter(film => 
            film.characters.some(character => character.includes(`/people/${characterId}/`))
        ).length;
        
        console.log(count);
    } catch (e) {
        console.error('Error parsing response:', e);
    }
});
