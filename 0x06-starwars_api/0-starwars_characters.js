#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people/?page=';

function fetchingData (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function main () {
  let i = 1;
  while (true) {
    const { response, body } = await fetchingData(`${url}${i}`);
    if (response.statusCode !== 200) {
      process.exit(0);
    }
    const charsList = await JSON.parse(body).results;
    // console.log(jsonList);
    charsList.forEach(char => {
      if (char.films.find(link => link.includes(movieID))) {
        console.log(char.name);
      }
    });
    i++;
  }
}

main();
