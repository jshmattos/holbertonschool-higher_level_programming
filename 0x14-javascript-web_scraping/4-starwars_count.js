#!/usr/bin/node

const request = require('request');

const url = 'http://swapi.co/api/people/18';
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
