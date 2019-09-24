#!/usr/bin/node

const request = require('request');

const wedge = 'https://swapi.co/api/people/18/';
request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((count, el) => {
      el.characters.forEach(e => {
	if (e.includes('18')) {
	  count++;
	}
      })
      return count;
    }, 0));
  }
});
