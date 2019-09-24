#!/usr/bin/node

const request = require('request');

const wedge = 'https://swapi.co/api/people/18/';
request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    films = JSON.parse(body).results;
    console.log(films.reduce((count, el) => {
      if (el.characters.includes(wedge)) {
        count++
      }
      return count
    }, 0))
  }
});
