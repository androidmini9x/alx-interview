#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieID = process.argv[2];
  request(`${API_URL}/films/${movieID}`, (error, resp, body) => {
    if (error || resp.statusCode != 200) {
      console.log(error);
    } else {
      const characters = JSON.parse(body).characters;
      const fetchCharacters = characters.map(c => {
        return new Promise((resolve, rej) => {
          request(c, (err, res, charBody) => {
            if (err) {
              rej(err);
            }
            resolve(JSON.parse(charBody).name);
          });
        });
      });

      Promise.all(fetchCharacters)
        .then(name => console.log(name.join('\n')))
        .catch(err => console.log(err))
    }
  });
}
